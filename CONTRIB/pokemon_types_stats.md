# Pokemon statistics generator scripts
- __pokemon_types_stats_average.awk__ = average stats based on type
- __pokemon_types_stats_minmax.awk__ = Minimum and maximum values for tpe stats

The minmax and average scripts provide simple examples of data collation and
display using Awk. Both scripts and their data files were generated in-class
during a Q&A seswsion for module 3. The data files are based on the pokemon.csv
file that can be found in the module 1 folder; originally written by
[Gilles Armand](https://gist.github.com/armgilles). The file has been modified
to contain fewer columns, no header, and only generation 1 Pokemon; to ease
the in-class demo. The modified file was generated using a simple pipeline
ontaining grep and cut.

Both scripts ise an associative array to collate data based on the *type 1*
field from the original data file; effectively generating metrics for each
of the generation 1 pokemon types.