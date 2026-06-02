
def build_profile_text(
    freelancer,
    skills
):
    return f"""
    Skills:
    {' '.join(skills)}

    Experience:
    {freelancer.experience_years} years

    Bio:
    {freelancer.bio}
    """