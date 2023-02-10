from flask import Flask, jsonify, request
from flask.views import MethodView
from db import Ad, Session
from schema import validate_create_ad
from errors import HttpError
from flask_bcrypt import Bcrypt

app = Flask('app')
bcrypt = Bcrypt(app)


@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    http_response = jsonify({'status': 'error', "description": error.message})
    http_response.status_code = error.status_code
    return http_response


def get_ad(ad_id: int, session: Session):
    ad = session.query(Ad).get(ad_id)
    if ad is None:
        raise HttpError(404, 'ad not found')
    return ad


class Advertisement(MethodView):
    def get(self, ad_id: int):
        with Session() as session:
            ad = get_ad(ad_id, session)
            return jsonify({'id': ad.id,
                            'title': ad.title,
                            'description': ad.description,
                            'creation_time': ad.creation_time,
                            'owner': ad.owner,
                            })
    def post(self):
        json_data = validate_create_ad(request.json)
        with Session() as session:
            new_ad = Ad(**json_data)
            session.add(new_ad)
            session.commit()
            return jsonify({'id': new_ad.id,
                            'title': new_ad.title,
                            'description': new_ad.description,
                            'creation_time': new_ad.creation_time,
                            'owner': new_ad.owner,
                            })

    def patch(self, ad_id: int):
        json_data = request.json
        with Session() as session:
            ad = get_ad(ad_id, session)
            for field, value in json_data.items():
                setattr(ad, field, value)
            session.add(ad)
            session.commit()
        return jsonify({'status': 'succes'})

    def delete(self, ad_id: int):
        with Session() as session:
            ad = get_ad(ad_id, session)
            session.delete(ad)
            session.commit()
            return jsonify({'status': 'succes'})


app.add_url_rule("/ads/<int:ad_id>/", view_func=Advertisement.as_view('advertisement'),
                 methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule("/ads", view_func=Advertisement.as_view('advertisement1'), methods=['POST'])


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)