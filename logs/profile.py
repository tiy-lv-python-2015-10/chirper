import pstats
p = pstats.Stats('chirps.000539ms.1449017574.prof')
p.strip_dirs().sort_stats('cumulative').print_stats()
