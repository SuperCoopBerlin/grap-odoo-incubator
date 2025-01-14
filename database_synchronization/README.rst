========================
Database Synchronization
========================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-grap%2Fgrap--odoo--incubator-lightgray.png?logo=github
    :target: https://github.com/grap/grap-odoo-incubator/tree/12.0/database_synchronization
    :alt: grap/grap-odoo-incubator

|badge1| |badge2| |badge3| 

This module can be used to synchronize two Odoo database that shares the
same code base.

It provides two features:

- a cron task to synchronize the module installed.

- an interface to synchronize data and create IDs mapping, between two instance;

**Table of contents**

.. contents::
   :local:

Configuration
=============

* Go to "Settings > Technical > Parameters > System parameters" and
  set information regarding the target Odoo instance, and the credencials,
  with the following keys :

1. ``database_synchronization.host`` : host of the target Odoo instance, without ``http://``. set only ``localhost`` or the ``myerp.mywebsite.tld``.

2. ``database_synchronization.port``: port the target Odoo instance. Typically ``8069`` for dev instance, or ``443`` for test or production instance.

3. ``database_synchronization.database``: name of the database.

4. ``database_synchronization.login`` and ``database_synchronization.password``: credential used for the authentication.

* This module depends on ``queue_job`` module that requires specific
  configuration to works properly. Make sure your config file is correctly set.
  See https://github.com/OCA/queue/tree/12.0/queue_job

You should update your ``odoo.cfg`` file to add a new channel named
``root.database_synchronization_install_module``:


.. code-block::

  [queue_job]
  channels = root:2,root.database_synchronization_install_module:1

Otherwise, you'll have a non blocking warning in your log, like this one.

.. code-block::

  WARNING ? odoo.addons.queue_job.jobrunner.channels: unknown channel root.database_synchronization_install_module, using root channel for job 23f6b872-1d2c-4003-bd38-a8486bbec664

Usage
=====

TODO

Known issues / Roadmap
======================

When synchronizing module installation for the first time, it
can take a big while. During the installation, some task could be failed.
In that case, simply restart the jobs.

.. code-block::

  File "/home/sylvain/grap_dev/grap-odoo-env-12.0/src/odoo/odoo/addons/base/models/ir_module.py", line 446, in button_immediate_install
    return self._button_immediate_function(type(self).button_install)
  File "/home/sylvain/grap_dev/grap-odoo-env-12.0/src/odoo/odoo/addons/base/models/ir_module.py", line 556, in _button_immediate_function
    raise UserError(_("The server is busy right now, module operations are not possible at"
  odoo.exceptions.UserError: ('The server is busy right now, module operations are not possible at this time, please try again later.', '')

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/grap/grap-odoo-incubator/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/grap/grap-odoo-incubator/issues/new?body=module:%20database_synchronization%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* GRAP

Contributors
~~~~~~~~~~~~

* Sylvain LE GAL (https://www.twitter.com/legalsylvain)

Maintainers
~~~~~~~~~~~

This module is part of the `grap/grap-odoo-incubator <https://github.com/grap/grap-odoo-incubator/tree/12.0/database_synchronization>`_ project on GitHub.

You are welcome to contribute.
