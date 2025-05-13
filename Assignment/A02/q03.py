from typing import List, Dict, Tuple, Set, Optional

def parse_puzzle(puzzle_str: str) -> List[List[int]]:
    
    return [[int(puzzle_str[i * 9 + j]) for j in range(9)] for i in range(9)]

def grid_to_str(grid: List[List[int]]) -> str:
    
    return ''.join(str(cell) for row in grid for cell in row)

def get_peers(row: int, col: int) -> Set[Tuple[int, int]]:
    
    peers = set()
    for k in range(9):
        peers.add((row, k))
        peers.add((k, col))
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            peers.add((i, j))
    peers.remove((row, col))
    return peers

def init_domains(grid: List[List[int]]) -> Dict[Tuple[int, int], Set[int]]:
    domains = {}
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                domains[(i, j)] = set(range(1, 10))
            else:
                domains[(i, j)] = {grid[i][j]}
    return domains

def ac3(domains: Dict[Tuple[int, int], Set[int]]) -> bool:
    
    queue = [(xi, xj) for xi in domains for xj in get_peers(*xi)]
    while queue:
        xi, xj = queue.pop(0)
        if revise(domains, xi, xj):
            if not domains[xi]:
                return False
            for xk in get_peers(*xi):
                if xk != xj:
                    queue.append((xk, xi))
    return True

def revise(domains: Dict[Tuple[int, int], Set[int]], xi: Tuple[int, int], xj: Tuple[int, int]) -> bool:
    revised = False
    to_remove = set()
    for x in domains[xi]:
        if all(x == y for y in domains[xj]):
            to_remove.add(x)
    if to_remove:
        domains[xi] -= to_remove
        revised = True
    return revised

def is_complete(domains: Dict[Tuple[int, int], Set[int]]) -> bool:
    return all(len(domains[var]) == 1 for var in domains)

def select_unassigned_variable(domains: Dict[Tuple[int, int], Set[int]]) -> Optional[Tuple[int, int]]:
    unassigned = [var for var in domains if len(domains[var]) > 1]
    if not unassigned:
        return None
    return min(unassigned, key=lambda var: len(domains[var]))

def backtrack(domains: Dict[Tuple[int, int], Set[int]]) -> Optional[Dict[Tuple[int, int], Set[int]]]:
    if is_complete(domains):
        return domains
    var = select_unassigned_variable(domains)
    if var is None:
        return None
    for value in sorted(domains[var]):
        new_domains = {v: set(domains[v]) for v in domains}
        new_domains[var] = {value}
        if ac3(new_domains):
            result = backtrack(new_domains)
            if result:
                return result
    return None

def solve_sudoku(puzzle_str: str) -> str:
    grid = parse_puzzle(puzzle_str)
    domains = init_domains(grid)
    ac3(domains)
    result = backtrack(domains)
    if result:
        solved_grid = [[list(result[(i, j)])[0] for j in range(9)] for i in range(9)]
        return grid_to_str(solved_grid)
    return ''

def solve_sudoku_file(input_lines: List[str]) -> List[str]:
    return [solve_sudoku(line.strip()) for line in input_lines if line.strip()] 