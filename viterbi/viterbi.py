import sys

states = ('Combo', 'Free')
 
observations = []
 
start_probability = {'Combo': 0.5, 'Free': 0.5}
 
transition_probability = {
   'Combo' : {'Combo': 0.6, 'Free': 0.4},
   'Free' : {'Combo': 0.3, 'Free': 0.7},
   }
 
emission_probability = {
   'Combo' : {'9l': 0.1, '9m': 0.3, '9h': 0.6, '7l': 0.1, '7m': 0.3, '7h': 0.6, '1l': 0.5, '1m': 0.4, '1h': 0.1,'2l': 0.5, '2m': 0.4, '2h': 0.1, '3l': 0.5, '3m': 0.4, '3h': 0.1,'4l': 0.5, '4m': 0.4, '4h': 0.1,'5l': 0.5, '5m': 0.4, '5h': 0.1,'6l': 0.5, '6m': 0.4, '6h': 0.1, '8l': 0.5, '8m': 0.4, '8h': 0.1},
   'Free' : {'9l': 0.1, '9m': 0.3, '9h': 0.6, '7l': 0.1, '7m': 0.3, '7h': 0.6, '1l': 0.1, '1m': 0.3, '1h': 0.6, '2l': 0.5, '2m': 0.4, '2h': 0.1, '3l': 0.5, '3m': 0.4, '3h': 0.1,'4l': 0.5, '4m': 0.4, '4h': 0.1,'5l': 0.5, '5m': 0.4, '5h': 0.1,'6l': 0.5, '6m': 0.4, '6h': 0.1, '8l': 0.5, '8m': 0.4, '8h': 0.1},
   }

def print_dptable(V):
    print "    ",
    for i in range(len(V)): print "%7s" % ("%d" % i),
    print
 
    for y in V[0].keys():
        print "%.4s: " % y,
        for t in range(len(V)):
            print "%.7s" % ("%f" % V[t][y]),
        print
 
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
 
    # Initialize base cases (t == 0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
 
    # Run Viterbi for t > 0
    for t in range(1,len(obs)):
        V.append({})
        newpath = {}
 
        for y in states:
            (prob, state) = max([(V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states])
            V[t][y] = prob
            newpath[y] = path[state] + [y]
 
        # Don't need to remember the old paths
        path = newpath
 
    print_dptable(V)
    (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
    return (prob, path[state])

def example():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)

def fill_observations():
    for n in range (1, len(sys.argv)):
        observations.append(sys.argv[n])

if __name__ == '__main__':

    fill_observations()
    print observations
    print example()
