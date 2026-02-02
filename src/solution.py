## Student Name:
## Student ID: 

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    
        # Validate requests structure
    for req in requests:
        if not isinstance(req, dict):
            raise ValueError("Each request must be a dictionary")

    # Check for unknown resources in requests
    for req in requests:
        for resource in req:
            if resource not in resources:
                return False

    # Check capacity constraints
    for resource, capacity in resources.items():
        total_required = sum(req.get(resource, 0) for req in requests)
        if total_required > capacity:
            return False

    return True

    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Args:
        resources : Dict[str, Number], Mapping from resource name to total available capacity.
        requests : List[Dict[str, Number]], List of requests. Each request is a mapping from resource name to the amount required.

    Returns:
        True if the allocation is feasible, False otherwise.

    """
    # TODO: Implement this function
    #raise NotImplementedError("suggest_slots function has not been implemented yet")