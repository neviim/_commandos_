# Cliente para instalar zabbix-agente no windows 10
#
# referenci de contrucao
# https://www.digitalocean.com/community/tutorials/how-to-create-a-puppet-module-to-automate-wordpress-installation-on-ubuntu-14-04


    :: 1 criar novo modulo zabbix_agent:

        $ cd /etc/puppet/code/environments/production/modules
        $ puppet module generate fcn-zabbix_agent --skip-interview

        $ cat /etc/puppet/code/environments/production/modules/zabbix_agent/metadata.json

            {
            "name": "fcn-zabbix_agent",
            "version": "0.1.0",
            "author": "fcn",
            "summary": null,
            "license": "Apache-2.0",
            "source": "",
            "project_page": null,
            "issues_url": null,
            "dependencies": [
                {
                "name": "puppetlabs-stdlib",
                "version_requirement": ">= 1.0.0"
                }
            ],
            "data_provider": null
            }

    :: 2 criar manifesto para isntalar zabbix-agent