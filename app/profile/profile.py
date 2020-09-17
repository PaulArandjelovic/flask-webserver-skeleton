from flask import Blueprint, render_template


# Blueprint Configuration
profile_bp = Blueprint(
    'profile_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/profile'
)


@profile_bp.route('/profile', methods=['GET'])
def user_profile():
    """Logged-in user profile page."""
    return render_template(
        'profile.jinja2',
        title='User Profile',
        template='profile-template'
    )
