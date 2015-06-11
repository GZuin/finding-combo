
combo_states = ('Combo', 'Free')
 
combo_start_probability = {'Combo': 0.5, 'Free': 0.5}
 
combo_transition_probability = {
   'Combo' : {'Combo': 0.6, 'Free': 0.4},
   'Free' : {'Combo': 0.3, 'Free': 0.7},
   }
 
combo_emission_probability = {
   'Combo' : {'9l': 0.1, '9m': 0.3, '9h': 0.6,
              '7l': 0.1, '7m': 0.3, '7h': 0.6,
              '1l': 0.5, '1m': 0.4, '1h': 0.1,
              '2l': 0.5, '2m': 0.4, '2h': 0.1,
              '3l': 0.5, '3m': 0.4, '3h': 0.1,
              '4l': 0.5, '4m': 0.4, '4h': 0.1,
              '5l': 0.5, '5m': 0.4, '5h': 0.1,
              '6l': 0.5, '6m': 0.4, '6h': 0.1,
              '8l': 0.5, '8m': 0.4, '8h': 0.1},
   'Free' :  {'9l': 0.1, '9m': 0.3, '9h': 0.6,
              '7l': 0.1, '7m': 0.3, '7h': 0.6,
              '1l': 0.1, '1m': 0.3, '1h': 0.6,
              '2l': 0.5, '2m': 0.4, '2h': 0.1,
              '3l': 0.5, '3m': 0.4, '3h': 0.1,
              '4l': 0.5, '4m': 0.4, '4h': 0.1,
              '5l': 0.5, '5m': 0.4, '5h': 0.1,
              '6l': 0.5, '6m': 0.4, '6h': 0.1,
              '8l': 0.5, '8m': 0.4, '8h': 0.1},
   }


input_states = ('1l', '1m', '1h', '2l', '2m', '2h', '3l', '3m', '3h',
                '4l', '4m', '4h', '5l', '5m', '5h', '6l', '6m', '6h',
                '7l', '7m', '7h', '8l', '8m', '8h', '9l', '9m', '9h', )
 
input_start_probability = {'1l': 0.037, '1m': 0.037, '1h': 0.037,
                           '2l': 0.037, '2m': 0.037, '2h': 0.037,
                           '3l': 0.037, '3m': 0.037, '3h': 0.037,
                           '4l': 0.037, '4m': 0.037, '4h': 0.037,
                           '5l': 0.037, '5m': 0.037, '5h': 0.037,
                           '6l': 0.037, '6m': 0.037, '6h': 0.037,
                           '7l': 0.037, '7m': 0.037, '7h': 0.037,
                           '8l': 0.037, '8m': 0.037, '8h': 0.037,
                           '9l': 0.037, '9m': 0.037, '9h': 0.037,}

 
input_transition_probability = {
   '1l' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '1m' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '1h' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '2l' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '2m' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '2h' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '3l' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '3m' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '3h' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '4l' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '4m' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '4h' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '5l' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '5m' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '5h' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '6l' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '6m' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '6h' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '7l' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '7m' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '7h' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '8l' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '8m' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '8h' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '9l' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '9m' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
   '9h' : {'1l': 0.037, '1m': 0.037, '1h': 0.037,
           '2l': 0.037, '2m': 0.037, '2h': 0.037,
           '3l': 0.037, '3m': 0.037, '3h': 0.037,
           '4l': 0.037, '4m': 0.037, '4h': 0.037,
           '5l': 0.037, '5m': 0.037, '5h': 0.037,
           '6l': 0.037, '6m': 0.037, '6h': 0.037,
           '7l': 0.037, '7m': 0.037, '7h': 0.037,
           '8l': 0.037, '8m': 0.037, '8h': 0.037,
           '9l': 0.037, '9m': 0.037, '9h': 0.037},
      }
 
input_emission_probability = {
    '1l' : {'Combo': 0.5, 'Free': 0.5},
    '1m' : {'Combo': 0.5, 'Free': 0.5},
    '1h' : {'Combo': 0.5, 'Free': 0.5},
    '2l' : {'Combo': 0.5, 'Free': 0.5},
    '2m' : {'Combo': 0.5, 'Free': 0.5},
    '2h' : {'Combo': 0.5, 'Free': 0.5},
    '3l' : {'Combo': 0.5, 'Free': 0.5},
    '3m' : {'Combo': 0.5, 'Free': 0.5},
    '3h' : {'Combo': 0.5, 'Free': 0.5},
    '4l' : {'Combo': 0.5, 'Free': 0.5},
    '4m' : {'Combo': 0.5, 'Free': 0.5},
    '4h' : {'Combo': 0.5, 'Free': 0.5},
    '5l' : {'Combo': 0.5, 'Free': 0.5},
    '5m' : {'Combo': 0.5, 'Free': 0.5},
    '5h' : {'Combo': 0.5, 'Free': 0.5},
    '6l' : {'Combo': 0.5, 'Free': 0.5},
    '6m' : {'Combo': 0.5, 'Free': 0.5},
    '6h' : {'Combo': 0.5, 'Free': 0.5},
    '7l' : {'Combo': 0.5, 'Free': 0.5},
    '7m' : {'Combo': 0.5, 'Free': 0.5},
    '7h' : {'Combo': 0.5, 'Free': 0.5},
    '8l' : {'Combo': 0.5, 'Free': 0.5},
    '8m' : {'Combo': 0.5, 'Free': 0.5},
    '8h' : {'Combo': 0.5, 'Free': 0.5},
    '9l' : {'Combo': 0.5, 'Free': 0.5},
    '9m' : {'Combo': 0.5, 'Free': 0.5},
    '9h' : {'Combo': 0.5, 'Free': 0.5},
   }
