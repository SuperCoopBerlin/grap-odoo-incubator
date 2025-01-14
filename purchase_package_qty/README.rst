===========================
Purchase - Package Quantity
===========================

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
    :target: https://github.com/grap/grap-odoo-incubator/tree/12.0/purchase_package_qty
    :alt: grap/grap-odoo-incubator

|badge1| |badge2| |badge3| 

This module extends the functionality of purchase module to support package
quantity.

In the product supplierinfo, add a "Package Qty" field to register how many
purchase UoM of the product there are in the package the supplier uses.
All purchase lines for this product+supplier must have a quantity that is a
multiple of that package quantity.

For example:

* A supplier sells beers with a price per unit, thus the purchase UoM is PCE.
* The supplier put them in 6pcs boxes, and the purchaser have to buy a multiple
  of 6.
* The supplier has a minimum quantity of 60.

So the settings of the product will be the following :

.. image:: https://raw.githubusercontent.com/grap/grap-odoo-incubator/12.0/purchase_package_qty/static/description/product_supplierinfo_form.png

**Table of contents**

.. contents::
   :local:

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/grap/grap-odoo-incubator/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/grap/grap-odoo-incubator/issues/new?body=module:%20purchase_package_qty%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* GRAP

Contributors
~~~~~~~~~~~~

* Julien WESTE
* Sylvain LE GAL (https://www.twitter.com/legalsylvain)

Maintainers
~~~~~~~~~~~

This module is part of the `grap/grap-odoo-incubator <https://github.com/grap/grap-odoo-incubator/tree/12.0/purchase_package_qty>`_ project on GitHub.

You are welcome to contribute.
