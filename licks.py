def total_licks(env):
   base_licks = 252
   max = 0
   max_key = 'nobody'
   str = 'It took %d licks to get to the tootsie roll center of a tootsie pop.'
   extra_str = ' The toughest challenge was %s.'
   final_licks = base_licks
   final_str = str % base_licks

   for k, v in env.iteritems():
      final_licks = final_licks + v
      if (v > max):
          max_k = k
          max = v
      final_str = str % final_licks
      if max > 0:
          final_str = final_str + (extra_str % max_k)
   return final_str
