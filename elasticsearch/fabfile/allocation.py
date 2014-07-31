from fabric.api import task, run


@task(name='disable')
def disable_allocation():
    cmd = "curl -X PUT http://localhost:9200/_cluster/settings -d '     \
            {                                                           \
                \"transient\": {                                        \
                    \"cluster.routing.allocation.enable\": \"none\"     \
                }                                                       \
            }'"
    run(cmd)


@task(name='enable')
def enable_allocation():
    cmd = "curl -X PUT http://localhost:9200/_cluster/settings -d '     \
            {                                                           \
                \"transient\": {                                       \
                    \"cluster.routing.allocation.enable\": \"all\"     \
                }                                                       \
            }'"
    run(cmd)


@task(name='check')
def check_allocation():
    cmd = 'curl -X GET http://localhost:9200/_cluster/settings?pretty=true'
    run(cmd)