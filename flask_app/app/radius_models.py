from app import app, db, admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.ext.automap import automap_base

# generate model classes based on the already created
# database (the engine is the postgres connection)
Base = automap_base()
Base.prepare(db.engine, reflect=True)

# get the model from the mapped database
RadAcct = Base.classes.radacct
RadCheck = Base.classes.radcheck
RadGroupCheck = Base.classes.radgroupcheck
RadGroupReply = Base.classes.radgroupreply
RadReply = Base.classes.radreply
RadUserGroup = Base.classes.radusergroup
RadPostAuth = Base.classes.radpostauth
Nas = Base.classes.nas

# generate CRUD pages for the database
admin.add_view(ModelView(RadAcct, db.session))
admin.add_view(ModelView(RadCheck, db.session))
admin.add_view(ModelView(RadGroupCheck, db.session))
admin.add_view(ModelView(RadGroupReply, db.session))
admin.add_view(ModelView(RadReply, db.session))
admin.add_view(ModelView(RadUserGroup, db.session))
admin.add_view(ModelView(RadPostAuth, db.session))
admin.add_view(ModelView(Nas, db.session))