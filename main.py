from flaskapp import create_app
from flaskapp.api.tables import db, Content
# import pandas as pd

app = create_app()


# actions = pd.read_excel('actions.xlsx')
# actions = actions.set_index('action_id').T.to_dict()

# with app.app_context():
#     for key, value in actions.items():
#         db.session.add(
#             Content(
#                 action_id = int(key),
#                 action_title = value['action_title'],
#                 action_description = value['action_description'],
#                 action_impact = value['action_impact'],
#                 action_image = value['action_image'],
#                 category = value['category'],
#                 rating = 0,
#                 comments = "{}".format({}),
#             )
#         )
#         db.session.commit()
#         actions = ""


if __name__ == '__main__':
    app.run(debug=True)

