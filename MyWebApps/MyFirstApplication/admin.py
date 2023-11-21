from django.contrib import admin

# Register your models here.
from .models.Category import Category
from .models.Challenge import Challenge
from .models.ChallengesCategory import ChallengesCategory
from .models.Comment import Comment
from .models.Follow import Follow
from .models.GroupChat import GroupChat
from .models.Member import Member
from .models.Message import Message
from .models.Notification import Notification
from .models.Participation import Participation
from .models.Post import Post
from .models.Preference import Preference
from .models.Reaction import Reaction
from .models.User import User
from .models.UsersPreference import UsersPreference

admin.site.register(Category)
admin.site.register(Challenge)
admin.site.register(ChallengesCategory)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(GroupChat)
admin.site.register(Member)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Participation)
admin.site.register(Post)
admin.site.register(Preference)
admin.site.register(Reaction)
admin.site.register(User)
admin.site.register(UsersPreference)