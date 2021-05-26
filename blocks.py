from planning import *
from search import Problem
from notebook import psource

def nworld():
        return PlanningProblem(initial='OnTable(A) & On(B, A) & On(C, B) & Clear(C) & OnTable(D) & On(E, D) & On(F, E) & Clear(F) & OnTable(G) & On(H, G) & On(I, H) & On(J, I) & Clear(J)', #representation of the intital state, all blocks at the top of towers are clear and can be moved
                                   goals='OnTable(A) & On(D, A) & On(G, D) & Clear(G) & OnTable(B) & On(E, B) & On(H, E) & Clear(H) & OnTable(C) & On(I, C) & Clear(I) & OnTable(J) & On(F, J) & Clear(F)', #representation of goal state
                                   actions=[Action('ToTable(x, y)', #action from planning.ipynb, used to move blocks from somewhere to the table
                                                   precond='On(x, y) & Clear(x)',
                                                   effect='~On(x, y) & Clear(y) & OnTable(x)'),
                                           Action('FromTable(y, x)', #action from planning.ipynb, used to move blocks from table to somewhere
                                                   precond='OnTable(y) & Clear(y) & Clear(x)',
                                                   effect='~OnTable(y) & ~Clear(x) & On(y, x)')],
                              )

neworld = nworld() #set up the problem
solution = [expr('ToTable(C,B)'), expr('ToTable(B,A)'), expr('ToTable(F,E)'), expr('ToTable(E,D)'), expr('ToTable(J,I)'), expr('ToTable(I,H)'), expr('ToTable(H,G)'), expr('FromTable(D,A)'), expr('FromTable(G,D)'), expr('FromTable(E,B)'), expr('FromTable(H,E)'), expr('FromTable(I,C)'), expr('FromTable(F,J)')] 
#above are the actions taken to reach the goal state from the intial state; unstack all blocks so they are all on the table; restack them in the desired order, starting from the leftmost tower
for action in solution: #print out all actions
    neworld.act(action)
    print(action)
print('Goal:', neworld.goal_test()) #check if the actions have led to the goal state