from alembic import op
import sqlalchemy as sa

revision = '0003'
down_revision = '0002'

def upgrade():
    op.create_table(
        'audit_logs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('action', sa.String),
        sa.Column('metadata', sa.String),
        sa.Column('created_at', sa.DateTime)
    )

def downgrade():
    op.drop_table('audit_logs')
