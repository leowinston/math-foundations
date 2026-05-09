import cvxpy as cp
import numpy as np
# Exercise 2.5 "Additional Exercises for Convex Optimization" by Boyd
    
def inConvexHull(C,x):
    # Constraints for convex hull
    theta = cp.Variable(C.shape[1])
    constraints = [theta >= 0, cp.sum(theta) == 1, C @ theta == x]
    prob = cp.Problem(cp.Minimize(0), constraints)
    prob.solve()
    
    if prob.status == 'optimal':
        print(f"Point {x} is in the convex hull of set C!")
        print(f"Weights: {theta.value}") # This is the convex combination
    else:
        print(f"Point {x} is not in the convex hull of set C.")
        
def inConicHull(C,x):
    # Constraints for conic hull do not require parameters to add to one
    theta = cp.Variable(C.shape[1])
    constraints = [theta >= 0, C @ theta == x]
    prob = cp.Problem(cp.Minimize(0), constraints)
    prob.solve()
    
    if prob.status == 'optimal':
        print(f"Point {x} is in the conic hull of set C!")
        print(f"Weights: {theta.value}")
    else:
        print(f"Point {x} is not in the conic hull of set C.")
    

if __name__ == '__main__':
    # Set C = {(1,0), (1,1), (-1,-1), (0,0)}
    C = np.array([[1, 1, -1, 0], [0, 1, -1, 0]])
    # Point (0,-1/3)
    x = np.array([0,-1/3])
    inConvexHull(C,x)
    
    # Point (0,1/3)
    x = np.array([0,1/3])
    inConvexHull(C,x)
    
    # Point (0,-1/3)
    x = np.array([0,1/3])
    inConicHull(C,x)
    
    # Point (-22.718,-22.718)
    x = np.array([-22.718,-22.718])
    inConicHull(C,x)
    
    # Point (52.22,52.23)
    x = np.array([52.22,52.23])
    inConicHull(C,x)