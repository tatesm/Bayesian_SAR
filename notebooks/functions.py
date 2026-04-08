import numpy as np
import math

def init_grid(rows, columns):

    grid = np.zeros((rows,columns))
    return grid


def prior_probability_distribution(distribution_type, **params):
    if distribution_type == "uniform":
        def uniform_function(i,j):
            score = 1
            return score
        return uniform_function

    elif distribution_type == "gaussian":
        # extract params
        cx = params["cx"]
        cy = params["cy"]
        sigma = params["sigma"]
        # define gaussian_function
        def gaussian_function(i,j):

            distance = math.sqrt((i-cx)**2+(j-cy)**2)
            score = np.exp((-distance**2)/(2*(sigma**2)))
            return score

        return gaussian_function

    else:
        raise ValueError("Unsupported distribution choice")
    
def apply_prior_distribution(grid, cell_probability_function):
    new_grid = np.zeros_like(grid)
    for (i, j), value in np.ndenumerate(grid):
        new_grid[i, j] = cell_probability_function(i,j)
        print(f"Index: ({i}, {j}), Cell Probability: {new_grid[i, j]}")
    return new_grid



def normalize_grid(grid):
    if np.isclose(np.sum(grid), 0):
        raise ValueError("Sum of filled grid is 0")
    normalized_grid = grid /np.sum(grid)
    if np.isclose(np.sum(normalized_grid),1):
        return normalized_grid
    else:
        raise ValueError(f"Normalized grid total probability != 1, total probability is {np.sum(normalized_grid)}")



def grid_update(cell: tuple, grid: np.ndarray, pod: float) -> np.ndarray:
    i, j = cell
    new_grid = grid.copy()
    new_grid[i,j] = new_grid[i,j] * (1-pod)
    new_sum = np.sum(new_grid)
    updated_grid = new_grid/new_sum
    if np.isclose(np.sum(updated_grid), 1):
        return updated_grid
    else:
        raise ValueError(f"Updated grid total probability != 1, total probability is {np.sum(updated_grid)}")



def choose_next_cell(current_grid: np.ndarray):
    k = np.argmax(current_grid)
    next_cell = np.unravel_index(k,current_grid.shape)
    return next_cell



def run_search(grid: np.ndarray, pod: float, steps: int) -> list: 
    search_history = []
    # grid_history = [] will be used in next version, to see how grid shifts and evolves

    for i in range(steps):
        cell = choose_next_cell(grid)
        search_history.append(cell)
        grid = grid_update(cell, grid, pod)
    return search_history