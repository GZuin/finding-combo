import sys
import hmm_tables as table

observations = []

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
    if (observations[0] == "Free" or observations[0] == "Combo"):
        return viterbi(observations,
                   table.input_states,
                   table.input_start_probability,
                   table.input_transition_probability,
                   table.input_emission_probability)
    else:
        return viterbi(observations,
                   table.combo_states,
                   table.combo_start_probability,
                   table.combo_transition_probability,
                   table.combo_emission_probability)

def fill_observations():
    for n in range (1, len(sys.argv)):
        observations.append(sys.argv[n])

def outside_observations(obs):
    observation = obs

if __name__ == '__main__':

    fill_observations()
    print observations
    print example()
