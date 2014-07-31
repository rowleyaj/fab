from fabric.api import task, run


@task()
def aliases():
    run("curl -XGET 'http://localhost:9200/_cat/aliases/?v'")


@task()
def allocation():
    run("curl -XGET 'http://localhost:9200/_cat/allocation/?v'")


@task()
def count():
    run("curl -XGET 'http://localhost:9200/_cat/count/?v'")


@task()
def fielddata():
    run("curl -XGET 'http://localhost:9200/_cat/fielddata/?v'")


@task()
def health():
    run("curl -XGET 'http://localhost:9200/_cat/health/?v'")


@task()
def indices():
    run("curl -XGET 'http://localhost:9200/_cat/indices/?v'")


@task()
def master():
    run("curl -XGET 'http://localhost:9200/_cat/master/?v'")


@task()
def nodes():
    run("curl -XGET 'http://localhost:9200/_cat/nodes/?v'")


@task()
def pending_tasks():
    run("curl -XGET 'http://localhost:9200/_cat/pending_tasks/?v'")


@task()
def plugins():
    run("curl -XGET 'http://localhost:9200/_cat/plugins/?v'")


@task()
def recovery():
    run("curl -XGET 'http://localhost:9200/_cat/recovery/?v'")


@task()
def thread_pool():
    run("curl -XGET 'http://localhost:9200/_cat/thread_pool/?v'")


@task()
def shards():
    run("curl -XGET 'http://localhost:9200/_cat/shards/?v'")