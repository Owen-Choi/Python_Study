import pandas as pd
import numpy as np
import featuretools as ft

clients = pd.read_csv('data/clients.csv', parse_dates=['joined'])
loans = pd.read_csv('data/loans.csv', parse_dates=['loan_start', 'loan_end'])
payments = pd.read_csv('data/payments.csv', parse_dates=['payment_date'])

es = ft.EntitySet(id='loans')
es = es.entity_from_dataframe(entity_id='loans', dataframe=loans, index='loan_id')

features, feature_names = ft.dfs(entityset=es, target_entity='loans',
                                 trans_primitives=['cum_sum'])
features


# import pandas as pd
# import numpy as np
# import featuretools as ft
#
# clients = pd.read_csv('data/clients.csv', parse_dates=['joined'])
# loans = pd.read_csv('data/loans.csv', parse_dates=['loan_start', 'loan_end'])
# payments = pd.read_csv('data/payments.csv', parse_dates=['payment_date'])
#
# es = ft.EntitySet(id='clients')
# es = es.entity_from_dataframe(entity_id='clients', dataframe=clients, index='client_id', time_index='joined')
# es = es.entity_from_dataframe(entity_id='loans', dataframe=loans, index='loan_id')
#
# es = es = es.entity_from_dataframe(entity_id='payments',
#                                    dataframe=payments,
#                                    variable_types={'missed': ft.variable_types.Categorical},
#                                    make_index=True,
#                                    index='payment_id',
#                                    time_index='payment_date')
#
# r_client_previous = ft.Relationship(es['clients']['client_id'],
#                                     es['loans']['client_id'])
#
# es = es.add_relationship(r_client_previous)
#
# r_payments = ft.Relationship(es['loans']['loan_id'],
#                              es['payments']['loan_id'])
#
# es = es.add_relationship(r_payments)
#
# features, feature_names = ft.dfs(entityset=es, target_entity='clients',
#                                  agg_primitives=['total'],
#                                  trans_primitives=['year', 'month'])  # 뒤에 subtract, devide가 더 있었는데
