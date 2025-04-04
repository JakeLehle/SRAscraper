import click
import cli.config
import cli.snakemake
from os import cpu_count

# IMPORTANT NOTE: All click arguments must be in lowercase!

@click.group()
def main():
    pass


@main.command(help='Create a config YAML file for running the SRAscrape pipeline.')
@click.option('--cores', type=click.INT, default=cpu_count()/2, help='The number of cores to use per job. Default is set to half the number of available cores.')
@click.argument('output_dir')
@click.argument('ncbi_search_txt')
@click.argument('target_yaml')
def create_config(cores, output_dir, ncbi_search_txt, target_yaml):

    cli.config.create_config(cores, output_dir, ncbi_search_txt, target_yaml)


@main.command(help='Run the SRAscraper pipeline using a config file.')
@click.option('--dry-run', is_flag=True, default=False, help='Only dry-run the workflow.')
@click.argument('config_yaml')
def run_config(dry_run, config_yaml):

    cli.snakemake.run_config(dry_run, config_yaml)

