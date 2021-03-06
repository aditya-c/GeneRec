from __future__ import unicode_literals

from django.db import models


class UserProfile(models.Model):
    user_id = models.CharField(('userid'), primary_key=True, max_length=10000)
    word_reading_ability = models.IntegerField(null=True, blank=True)
    white_wine_liking = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    vitamin_e = models.IntegerField(null=True, blank=True)
    vitamin_d = models.IntegerField(null=True, blank=True)
    vitamin_b12 = models.IntegerField(null=True, blank=True)
    vitamin_a = models.IntegerField(null=True, blank=True)
    type_2_diabetes = models.IntegerField(null=True, blank=True)
    smoking_behavior = models.IntegerField(null=True, blank=True)
    smell_sensitivity_for_malt = models.IntegerField(null=True, blank=True)
    skin_pigmentation = models.IntegerField(null=True, blank=True)
    reward_dependence = models.IntegerField(null=True, blank=True)
    response_to_vitamin_e_supplementation = models.IntegerField(null=True, blank=True)
    red_wine_liking = models.IntegerField(null=True, blank=True)
    red_hair = models.IntegerField(null=True, blank=True)
    reading_and_spelling_ability = models.IntegerField(null=True, blank=True)
    protein_intake = models.IntegerField(null=True, blank=True)
    prostate_cancer = models.IntegerField(null=True, blank=True)
    phosphorus = models.IntegerField(null=True, blank=True)
    peanuts_allergy = models.IntegerField(null=True, blank=True)
    pancreatic_cancer = models.IntegerField(null=True, blank=True)
    openness = models.IntegerField(null=True, blank=True)
    novelty_seeking = models.IntegerField(null=True, blank=True)
    nicotine_dependence = models.IntegerField(null=True, blank=True)
    neuroticism = models.IntegerField(null=True, blank=True)
    myocardial_infarction = models.IntegerField(null=True, blank=True)
    motion_sickness = models.IntegerField(null=True, blank=True)
    morning_person = models.IntegerField(null=True, blank=True)
    milk_allergy = models.IntegerField(null=True, blank=True)
    male_pattern_baldness_aga = models.IntegerField(null=True, blank=True)
    magnesium = models.IntegerField(null=True, blank=True)
    lung_cancer = models.IntegerField(null=True, blank=True)
    longevity = models.IntegerField(null=True, blank=True)
    lobe_size = models.IntegerField(null=True, blank=True)
    liver_cancer = models.IntegerField(null=True, blank=True)
    iron = models.IntegerField(null=True, blank=True)
    hearing_function = models.IntegerField(null=True, blank=True)
    harm_avoidance = models.IntegerField(null=True, blank=True)
    handedness = models.IntegerField(null=True, blank=True)
    gastric_cancer = models.IntegerField(null=True, blank=True)
    gambling = models.IntegerField(null=True, blank=True)
    freckles = models.IntegerField(null=True, blank=True)
    folate = models.IntegerField(null=True, blank=True)
    eye_color = models.IntegerField(null=True, blank=True)
    extraversion = models.IntegerField(null=True, blank=True)
    endurance_performance = models.IntegerField(null=True, blank=True)
    egg_allergy = models.IntegerField(null=True, blank=True)
    depression = models.IntegerField(null=True, blank=True)
    conscientiousness = models.IntegerField(null=True, blank=True)
    colorectal_cancer = models.IntegerField(null=True, blank=True)
    childhood_intelligence = models.IntegerField(null=True, blank=True)
    carbohydrate_intake = models.IntegerField(null=True, blank=True)
    calcium = models.IntegerField(null=True, blank=True)
    caffeine_metabolite_ratio = models.IntegerField(null=True, blank=True)
    caffeine_consumption = models.IntegerField(null=True, blank=True)
    breast_cancer = models.IntegerField(null=True, blank=True)
    bmi = models.IntegerField(null=True, blank=True)
    black_hair = models.IntegerField(null=True, blank=True)
    bitter_taste = models.IntegerField(null=True, blank=True)
    beta_carotene = models.IntegerField(null=True, blank=True)
    beard_thickness = models.IntegerField(null=True, blank=True)
    anger = models.IntegerField(null=True, blank=True)
    alpha_linolenic_acid = models.IntegerField(null=True, blank=True)
    alcohol_drinking_behavior = models.IntegerField(null=True, blank=True)
    agreeableness = models.IntegerField(null=True, blank=True)
    cluster_name = models.CharField(max_length=10000, null=True, blank=True)
    password = models.CharField(max_length=10000, default='pass', null=False, blank=False)
    cluster_name = models.CharField(max_length=10000, null=True, blank=True)
    authenticated = models.IntegerField(default=0)


class Movie(models.Model):
    movie_id = models.CharField(primary_key=True, max_length=10000)
    budget = models.FloatField(null=True, blank=True)
    genres = models.CharField(null=True, blank=True, max_length=10000)
    homepage = models.CharField(null=True, blank=True, max_length=10000)
    title = models.CharField(max_length=10000)
    overview = models.CharField(null=True, blank=True, max_length=10000)
    tagline = models.CharField(null=True, blank=True, max_length=10000)
    vote_average = models.FloatField(null=True, blank=True)
    release_date = models.CharField(null=True, blank=True, max_length=10000)
    production_companies = models.CharField(null=True, blank=True, max_length=10000)
    spoken_languages = models.CharField(null=True, blank=True, max_length=10000)


class UserMovieMap(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(UserProfile)
    rating = models.IntegerField(null=True, blank=True)


class UserMedoids(models.Model):
    cluster_name = models.CharField(max_length=12)
    user_id = models.CharField(max_length=10000)


class Song(models.Model):
    name = models.CharField(max_length=10000, null=True, blank=True)
    artist = models.CharField(max_length=10000, null=True, blank=True)


class UserSongMap(models.Model):
    user = models.ForeignKey(UserProfile)
    song = models.ForeignKey(Song)
    rating = models.IntegerField(null=True, blank=True)


class Puzzle(models.Model):
    difficulty = models.IntegerField()
    hyperlink = models.CharField(max_length=4000)
    image_hyperlink = models.CharField(max_length=4000)


class Book(models.Model):
    title = models.CharField(max_length=10000, null=True, blank=True)
    isbn = models.CharField(max_length=100, null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)
    ratings_count = models.IntegerField(null=True, blank=True)
    image_url = models.CharField(max_length=10000, null=True, blank=True)


class UserBookMap(models.Model):
    user = models.ForeignKey(UserProfile)
    book = models.ForeignKey(Book)
    rating = models.IntegerField(null=True, blank=True)
