from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Text
import uuid
import datetime
from sqlalchemy.ext.declarative import declarative_base, declared_attr
import hashlib
from pattern.en import pluralize

def uuid_gen():
    return str(uuid.uuid4())

class Base(object):
    @declared_attr
    def __tablename__(cls):
        return pluralize(cls.__name__.lower())

    id = Column(String(50), primary_key=True, default=uuid_gen)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)

    def to_json(self, **kwargs):
        obj = {}
        columns = [str(key).split(".")[1] for key in self.__table__.columns]
        skipList = ['id'] + kwargs.get('skipList', [])
        limitList = kwargs.get('limitList', columns)
        for key in limitList:
            if key not in skipList:
                value = getattr(self, key)
                try:
                    obj[key] = str(value)
                except Exception as e:
                    pass
        return obj

Base = declarative_base(cls=Base)


class User(Base):
    wwuid = Column(String(7), unique=True)
    username = Column(String(250), nullable=False)
    full_name = Column(String(250))
    status = Column(String(250))
    roles = Column(String(500))


class Profile(Base):
    wwuid = Column(String(7), ForeignKey('users.wwuid'), nullable=False)
    username = Column(String(250))
    full_name = Column(String(250))
    photo = Column(String(250))
    gender = Column(String(250))
    birthday = Column(String(250))
    email = Column(String(250))
    phone = Column(String(250))
    website = Column(String(250))
    majors = Column(String(500))
    minors = Column(String(500))
    graduate = Column(String(250))
    preprofessional = Column(String(250))
    class_standing = Column(String(250))
    high_school = Column(String(250))
    class_of = Column(String(250))
    relationship_status = Column(String(250))
    attached_to = Column(String(250))
    quote = Column(String(1000))
    quote_author = Column(String(250))
    hobbies = Column(String(500))
    career_goals = Column(String(1000))
    favorite_books = Column(String(1000))
    favorite_food = Column(String(1000))
    favorite_movies = Column(String(1000))
    favorite_music = Column(String(1000))
    pet_peeves = Column(String(500))
    personality = Column(String(250))
    views = Column(Integer)
    privacy = Column(Integer)
    department = Column(String(250))
    office = Column(String(250))
    office_hours = Column(String(250))

    def base_info(self):
        return self.to_json(limitList=['username', 'full_name', 'photo', 'email', 'views'])

class Volunteer(Base):
    wwuid = Column(String(7), ForeignKey('users.wwuid'), nullable=False)
    campus_ministries = Column(Boolean, default=False)
    student_missions = Column(Boolean, default=False)
    aswwu = Column(Boolean, default=False)
    circle_church = Column(Boolean, default=False)
    university_church = Column(Boolean, default=False)
    buddy_program = Column(Boolean, default=False)
    assist = Column(Boolean, default=False)
    lead = Column(Boolean, default=False)
    audio_slash_visual = Column(Boolean, default=False)
    health_promotion = Column(Boolean, default=False)
    construction_experience = Column(Boolean, default=False)
    outdoor_slash_camping = Column(Boolean, default=False)
    concert_assistance = Column(Boolean, default=False)
    event_set_up = Column(Boolean, default=False)
    children_ministries = Column(Boolean, default=False)
    children_story = Column(Boolean, default=False)
    art_poetry_slash_painting_slash_sculpting = Column(Boolean, default=False)
    organizing_events = Column(Boolean, default=False)
    organizing_worship_opportunities = Column(Boolean, default=False)
    organizing_community_outreach = Column(Boolean, default=False)
    bible_study = Column(Boolean, default=False)
    wycliffe_bible_translator_representative = Column(Boolean, default=False)
    food_preparation = Column(Boolean, default=False)
    graphic_design = Column(Boolean, default=False)
    poems_slash_spoken_word = Column(Boolean, default=False)
    prayer_team_slash_prayer_house = Column(Boolean, default=False)
    dorm_encouragement_and_assisting_chaplains = Column(Boolean, default=False)
    scripture_reading = Column(Boolean, default=False)
    speaking = Column(Boolean, default=False)
    videography = Column(Boolean, default=False)
    drama = Column(Boolean, default=False)
    public_school_outreach = Column(Boolean, default=False)
    retirement_slash_nursing_home_outreach = Column(Boolean, default=False)
    helping_the_homeless_slash_disadvantaged = Column(Boolean, default=False)
    working_with_youth = Column(Boolean, default=False)
    working_with_children = Column(Boolean, default=False)
    greeting = Column(Boolean, default=False)
    shofar_for_vespers = Column(Boolean, default=False)
    music = Column(String(250), default=False)
    join_small_groups = Column(Boolean, default=False)
    lead_small_groups = Column(Boolean, default=False)
    can_transport_things = Column(Boolean, default=False)
    languages = Column(String(250), default=False)
    wants_to_be_involved = Column(Boolean, default=False)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)

    # def to_json(self):
    #     return {'campus_ministries': str(self.campus_ministries),
    #             'student_missions': str(self.student_missions),'aswwu': str(self.aswwu),'circle_church': str(self.circle_church),'university_church': str(self.university_church),'buddy_program': str(self.buddy_program),\
    #             'assist': str(self.assist),'lead': str(self.lead),'audio_slash_visual': str(self.audio_slash_visual),'health_promotion': str(self.health_promotion),\
    #             'construction_experience': str(self.construction_experience),'outdoor_slash_camping': str(self.outdoor_slash_camping),'concert_assistance': str(self.concert_assistance),\
    #             'event_set_up': str(self.event_set_up),'children_ministries': str(self.children_ministries),'children_story': str(self.children_story),\
    #             'art_poetry_slash_painting_slash_sculpting': str(self.art_poetry_slash_painting_slash_sculpting),'organizing_events': str(self.organizing_events),\
    #             'organizing_worship_opportunities': str(self.organizing_worship_opportunities),'organizing_community_outreach': str(self.organizing_community_outreach),\
    #             'bible_study': str(self.bible_study),'wycliffe_bible_translator_representative': str(self.wycliffe_bible_translator_representative),\
    #             'food_preparation': str(self.food_preparation),'graphic_design': str(self.graphic_design),'poems_slash_spoken_word': str(self.poems_slash_spoken_word),\
    #             'prayer_team_slash_prayer_house': str(self.prayer_team_slash_prayer_house),'dorm_encouragement_and_assisting_chaplains': str(self.dorm_encouragement_and_assisting_chaplains),\
    #             'scripture_reading': str(self.scripture_reading),'speaking': str(self.speaking),'videography': str(self.videography),'drama': str(self.drama),\
    #             'public_school_outreach': str(self.public_school_outreach),'retirement_slash_nursing_home_outreach': str(self.retirement_slash_nursing_home_outreach),\
    #             'helping_the_homeless_slash_disadvantaged': str(self.helping_the_homeless_slash_disadvantaged),'working_with_youth': str(self.working_with_youth),\
    #             'working_with_children': str(self.working_with_children),'greeting': str(self.greeting),'shofar_for_vespers': str(self.shofar_for_vespers),\
    #             'music': str(self.music), 'join_small_groups': str(self.join_small_groups), 'lead_small_groups': str(self.lead_small_groups),\
    #             'can_transport_things': str(self.can_transport_things), 'languages': str(self.languages), 'wants_to_be_involved': str(self.wants_to_be_involved)}

    def only_true(self):
        fields = ['campus_ministries','student_missions','aswwu','circle_church','university_church','assist','lead','audio_slash_visual','health_promotion','construction_experience','outdoor_slash_camping','concert_assistance','event_set_up','children_ministries','children_story','art_poetry_slash_painting_slash_sculpting','organizing_events','organizing_worship_opportunities','organizing_community_outreach','bible_study','wycliffe_bible_translator_representative','food_preparation','graphic_design','poems_slash_spoken_word','prayer_team_slash_prayer_house','dorm_encouragement_and_assisting_chaplains','scripture_reading','speaking','videography','drama','public_school_outreach','retirement_slash_nursing_home_outreach','helping_the_homeless_slash_disadvantaged','working_with_youth','working_with_children','greeting','shofar_for_vespers','music','join_small_groups','lead_small_groups','can_transport_things','languages','wants_to_be_involved']
        data = []
        for f in fields:
            if getattr(self, f) == True:
                data.append(str(f))
            elif getattr(self, f) != '':
                if f == 'music':
                    data.append({'music': self.music})
                elif f == 'languages':
                    data.append({'languages': self.languages})
        return data


# class CollegianArticle(Base):
#     __tablename__ = "collegian_articles"
#     id = Column(String(50), primary_key=True, default=uuid_gen)
#     volume = Column(Integer, nullable=False)
#     issue = Column(Integer, nullable=False)
#     title = Column(String(500), nullable=False)
#     author = Column(String(500), nullable=False)
#     section = Column(String(500), nullable=False)
#     content = Column(Text, nullable=False)
#     updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
#     def to_json(self):
#         return {'id': str(self.id), 'volume': str(self.volume), 'issue': str(self.issue), 'title': str(self.title), 'author': str(self.author), 'section': str(self.section), 'content': self.content.encode('utf-8', 'ignore'), 'updated_at': str(self.updated_at)}


# class ElectionVote(Base):
#     __tablename__ = "election_votes"
#     id = Column(String(50), primary_key=True, default=uuid_gen)
#     wwuid = Column(String(7), ForeignKey("users.wwuid"))
#     executive_vp = Column(String(200), nullable=False)
#     social_vp = Column(String(200), nullable=False)
#     spiritual_vp = Column(String(200), nullable=False)
#     president = Column(String(200), nullable=False)
#     updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
#     def to_json(self):
#         return {'id': str(self.id), 'executive_vp': str(self.executive_vp), 'social_vp': str(self.social_vp), 'spiritual_vp': str(self.spiritual_vp), 'president': str(self.president)}


class TownathlonEntry(Base):
    # __tablename__ = "townathlon_entries"
    # id = Column(String(50), primary_key=True, default=uuid_gen)
    name = Column(String(500))
    email = Column(String(500))
    phone = Column(String(500))
    age = Column(String(500))
    address_1 = Column(String(500))
    address_2 = Column(String(500))
    city = Column(String(500))
    state = Column(String(500))
    zipcode = Column(String(500))
    # def to_json(self):
    #     return {'id': str(self.id), 'name': str(self.name), 'email': str(self.email), 'phone': str(self.phone), 'age': str(self.age), 'address_1': str(self.address_1), 'address_2': str(self.address_2), 'city': str(self.city), 'state': str(self.state), 'zipcode': str(self.zipcode)}
