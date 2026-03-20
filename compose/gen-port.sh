echo $(docker ps --format "table {{.Names}}\t{{.Ports}}") > /lab/compose/ports
