===========
Graphql CRM
===========

The purpose of this repository is to demonstrate how simple it is to
expose Odoo's data with GraphQL, by using OCA module 
`graphql_base <https://github.com/OCA/rest-framework>`_.

Requirements
============

Feel free to use `docker-compose <https://docs.docker.com/compose/install/>`_
to have an installation of Odoo ready-to-use for this demonstration.

Simply create a new database with Odoo 13.0 CE or Odoo 13.0 EE,
then install module `graphql_crm`.

Usage
=====

Test on GraphiQL
~~~~~~~~~~~~~~~~

Access to your database on: http://localhost:8099/graphiql/demo

You can now play with queries. Here is an example to get all opportunities
present in your database, including main information of their contact.

.. code-block::

    {
        allOpportunities {
            contact {
            street
            street2
            city
            zip
            email
            phone
            }
        }
    }

Use Python requests library
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test your first resolver:

.. code-block:: python

    import requests

    sess = requests.session()
    data = {
        "jsonrpc": "2.0", 
        "method": "call", 
        "params": {
            "db": "test", 
            "login": "admin", 
            "password": "admin",
        },
    }
    sess.post('http://127.0.0.1:8099/web/session/authenticate', json=data)
    response = sess.get(
        'http://127.0.0.1:8099/graphql/demo', 
        json={'query': '{ reverse(word: "hello world") }'})

    print(response.status_code)
    print(response.content)