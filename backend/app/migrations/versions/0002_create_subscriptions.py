from alembic import op
import sqlalchemy as sa

revision = '0002'
down_revision = '0001'

def upgrade():
    op.create_table(
        'subscriptions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('plan', sa.String),
        sa.Column('provider', sa.String),
        sa.Column('status', sa.String),
        sa.Column('started_at', sa.DateTime)
    )

def downgrade():
    op.drop_table('subscriptions')
