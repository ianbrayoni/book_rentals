<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

- [Book Rental Challenge](#book-rental-challenge)
  - [Approach](#approach)
  - [Coverage Report](#coverage-report)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Book Rental Challenge

## Approach

This service provides a restful `POST` API endpoint to calculate the charges of a book and return an invoice statement.

The API has been documented [here](openapi/schema.yaml)

## Coverage Report

The test coverage report has been facilitated by [coverage.py](https://coverage.readthedocs.io/)

```
Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
api/__init__.py                      0      0   100%
api/admin.py                         1      0   100%
api/apps.py                          3      0   100%
api/migrations/0001_initial.py       6      0   100%
api/migrations/__init__.py           0      0   100%
api/models.py                       12      0   100%
api/permissions.py                   7      0   100%
api/serializers.py                   7      0   100%
api/urls.py                          3      0   100%
api/views.py                        21      0   100%
book_rentals/__init__.py             0      0   100%
book_rentals/settings.py            24      0   100%
book_rentals/urls.py                 5      0   100%
charging/__init__.py                 0      0   100%
charging/book.py                    33      0   100%
charging/calculate.py               29      0   100%
manage.py                           12      2    83%   11-12
utils/__init__.py                    0      0   100%
utils/helpers.py                    19      0   100%
--------------------------------------------------------------
TOTAL                              182      2    99%
```
