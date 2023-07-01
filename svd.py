from surprise import Dataset, Reader
reader = Reader(rating_scale=(min_rating, max_rating))
data = Dataset.load_from_df(data[['userId', 'movieId', 'rating']], reader)


from surprise import BaselineOnly
from surprise.model_selection import cross_validate

cross_validate(BaselineOnly(), data, verbose=True)


from surprise import SVD
from surprise.model_selection import GridSearchCV
from surprise import accuracy
 
param_grid = {
  'n_factors': [20, 50, 100],
  'n_epochs': [5, 10, 20, 30, 40, 50],
  "lr_all": [0.001,0.002, 0.005],
  "reg_all": [0.4, 0.6]
}
 
gs = GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=3, n_jobs=-1)
gs.fit(data)
 
print(gs.best_score['rmse'])
print(gs.best_params['rmse'])


# O algo possui os melhorar parametros
algo = gs.best_estimator["rmse"]



trainset, testset = train_test_split(data, test_size=.20)


algo.fit(trainset)	


from collections import defaultdict

def get_top_n(predictions, n=10):
    """Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    """

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n



predictions = algo.test(testset)


top_n = get_top_n(predictions, n=10)

# Print the recommended items for each user
for uid, user_ratings in top_n.items():
    print(uid, [iid for (iid, _) in user_ratings])