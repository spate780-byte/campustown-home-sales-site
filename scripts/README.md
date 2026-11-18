# Scripts

Scripts that make data files for the site go here. The city median summary is generated with:

```sh
python scripts/make_city_median_prices.py
```

If the site reads a file that a script made, commit both the script and the file it makes. Say in the main README how to run the script, so anyone can rerun it and get the same file.

Unless you switch to a framework that needs a build step (and update `.github/workflows/pages.yml` to match), the site must work as committed: GitHub Pages publishes the files as they are.
