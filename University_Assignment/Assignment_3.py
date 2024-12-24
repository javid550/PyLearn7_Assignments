import time
import random

# تعریف گراف
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# دامنه رنگ‌ها
colors = ['Red', 'Green', 'Blue']

def is_valid(node, color, assignment):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


# پیاده سازی روش بکترکینگ
def backtrack(assignment):
    if len(assignment) == len(graph):
        return assignment
    
    unassigned = [node for node in graph if node not in assignment]
    node = unassigned[0]
    
    for color in colors:
        if is_valid(node, color, assignment):
            assignment[node] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[node]  # Backtrack

    return None

# اجرای بکترکینگ
start_time = time.time()
solution = backtrack({})
end_time = time.time()

print("Backtracking Solution:", solution)
print("Backtracking Time:", end_time - start_time)

# استفاده از فیلترها(Filtering)
def forward_checking(node, color, assignment):
    # ایجاد یک کپی از دامنه‌ها
    local_colors = colors[:]
    
    # کاهش دامنه همسایه هامون
    for neighbor in graph[node]:
        if neighbor not in assignment:
            if color in local_colors:
                local_colors.remove(color)

    return local_colors

def backtrack_with_filtering(assignment):
    if len(assignment) == len(graph):
        return assignment
    
    unassigned = [node for node in graph if node not in assignment]
    node = unassigned[0]
    
    for color in forward_checking(node, colors, assignment):
        if is_valid(node, color, assignment):
            assignment[node] = color
            result = backtrack_with_filtering(assignment)
            if result:
                return result
            del assignment[node]  # Backtrack

    return None

# اجرای بکترکینگ با فیلتر
start_time = time.time()
solution_filtering = backtrack_with_filtering({})
end_time = time.time()

print("Backtracking with Filtering Solution:", solution_filtering)
print("Backtracking with Filtering Time:", end_time - start_time)


# مرتب سازی
def select_variable(assignment):
    unassigned = [node for node in graph if node not in assignment]
    return min(unassigned, key=lambda node: len(forward_checking(node, None, assignment)))

def backtrack_with_ordering(assignment):
    if len(assignment) == len(graph):
        return assignment
    
    node = select_variable(assignment)
    
    for color in forward_checking(node, colors, assignment):
        if is_valid(node, color, assignment):
            assignment[node] = color
            result = backtrack_with_ordering(assignment)
            if result:
                return result
            del assignment[node]  # Backtrack

    return None

# اجرای بکترکینگ با مرتب‌سازی
start_time = time.time()
solution_ordering = backtrack_with_ordering({})
end_time = time.time()

print("Backtracking with Ordering Solution:", solution_ordering)
print("Backtracking with Ordering Time:", end_time - start_time)



# جستوجوی محلی (local search)
def local_search():
    # شروع با یک رنگ تصادفی برای هر راس
    current_assignment = {node: random.choice(colors) for node in graph}
    
    def get_cost(assignment):
        cost = 0
        for node in graph:
            for neighbor in graph[node]:
                if neighbor in assignment and assignment[node] == assignment[neighbor]:
                    cost += 1
        return cost

    current_cost = get_cost(current_assignment)
    
    while current_cost > 0:
        for node in current_assignment:
            original_color = current_assignment[node]
            for color in colors:
                current_assignment[node] = color
                new_cost = get_cost(current_assignment)
                if new_cost < current_cost:
                    current_cost = new_cost
                    break
            else:
                current_assignment[node] = original_color  # Backtrack to original color

    return current_assignment

# اجرای جستجوی محلی
start_time = time.time()
local_solution = local_search()
end_time = time.time()

print("Local Search Solution:", local_solution)
print("Local Search Time:", end_time - start_time)


# مقایسه نتیجه ها
# مقایسه نتایج
print("\nSummary of Results:")
print("Backtracking Solution:", solution)
print("Backtracking with Filtering Solution:", solution_filtering)
print("Backtracking with Ordering Solution:", solution_ordering)
print("Local Search Solution:", local_solution)
