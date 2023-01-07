from django.db import models
from django.contrib.auth.models import User
import datetime, os

from django.dispatch import receiver
####=====================custom user model=======================
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser, Group
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, campus, password=None, **kwargs):
        if not username:
            raise ValueError('Accounts must have a  username')
        if not first_name:
            raise ValueError('Accounts must have a  first name')
        if not last_name:
            raise ValueError('Accounts must have a  last name')
        if not campus:
            raise ValueError('Accounts must have a  campus')
        user = self.model(username=username, first_name=first_name, last_name=last_name, campus=campus)
        self.password = make_password(password)
        user.set_password(self.password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, campus, password):
        user = self.model(first_name=first_name, last_name=last_name,
                          password=make_password(password),
                          username=username, campus=campus)

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True, null=True)
    c = (('Akpugo', 'Akpugo'),
         ('Elele', 'Elele'),
         ('Okija', 'Okija'),
         ('National', 'National'),
         ('None', 'None'),)
    campus = models.CharField(choices=c, max_length=255, verbose_name='campus', )
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(verbose_name='first name', max_length=255)
    last_name = models.CharField(verbose_name='last name', max_length=255)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'campus']

    objects = UserManager()

    def __str__(self):
        self.name = f"{self.first_name} {self.last_name}"
        return self.name

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


# Create your models here.

class Campus(models.Model):
    campus = models.CharField(verbose_name='Name', max_length=255)
    location = models.CharField(verbose_name='Location', max_length=255, null=True, blank=True)
    history = models.TextField(verbose_name='Brief History', max_length=255, null=True, blank=True)
    numerical_strength = models.IntegerField(verbose_name='number of members', null=True, blank=True)
    phone_num = models.CharField(verbose_name='Phone number', max_length=255, null=True, blank=True)
    account_num = models.CharField(verbose_name='Account number', max_length=255, null=True, blank=True)
    account_bank = models.CharField(verbose_name='Account Bank', max_length=255, null=True, blank=True)
    date_created = models.DateField(verbose_name='The date the Choir was Created', null=True, blank=True)

    def __str__(self):
        return f'{self.campus}'

    class Meta:
        verbose_name = "Campus"
        verbose_name_plural = "Campuses"


class Profile_Akpugo(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, )
    firstname = models.CharField(verbose_name='First Name', max_length=255)
    lastname = models.CharField(verbose_name='Last Name', max_length=255)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True, null=True)
    g = (('Male', 'Male'),
         ('Female', 'Female'),)
    gender = models.CharField(choices=g, default='Male', verbose_name='Gender', max_length=255)
    phone_num = models.CharField(verbose_name='Phone number', max_length=255, blank=True)
    department = models.CharField(default='none', verbose_name='Department', max_length=255)

    p = (('Soprano', 'Soprano'),
         ('Alto', 'Alto'),
         ('Tenor', 'Tenor'),
         ('Bass', 'Bass'),
         ('None', 'None'),)
    part = models.CharField(choices=p, help_text='The part of the person', max_length=100)
    c = (('Akpugo', 'Akpugo'),
         ('None', 'None'),)
    campus = models.CharField(choices=c, default='Akpugo', max_length=255)
    s = (('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'),
         ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'),
         ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'),
         ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'),
         ('Ekiti State', 'Ekiti State'),
         ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'),
         ('Jigawa State', 'Jigawa State'),
         ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kebbi State', 'Kebbi State'),
         ('Kogi State', 'Kogi State'),
         ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'),
         ('Niger State', 'Niger State'),
         ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'),
         ('Oyo State', 'Oyo State'),
         ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'),
         ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State'),
         )
    state = models.CharField(choices=s, verbose_name='State', max_length=255, blank=True)
    m = (('Single', 'Single'),
         ('Married', 'Married'),
         ('Religious', 'Religious'),
         )
    marital_status = models.CharField(choices=m, verbose_name='Marital Status', max_length=255, blank=True)
    birthday = models.DateField(default='1999-01-01', verbose_name='Birth Day', null=True, blank=True)
    joindate = models.DateField(default='1999-01-01', verbose_name='Join Date', null=True, blank=True)
    graduatedate = models.DateField(default='1999-01-01', verbose_name='Graduate Date', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.firstname} {self.lastname})"

    class Meta:
        verbose_name = "Profile (Akpugo)"
        verbose_name_plural = "Profile (Akpugo)"


class Position_Akpugo(models.Model):
    campus = models.CharField(default='Akpugo', max_length=255, editable=False)
    pos = models.CharField(verbose_name='Position', help_text='Enter the position in full', max_length=255)

    def __str__(self):
        return f'{self.pos} (Akpugo)'

    class Meta:
        verbose_name = "Position (Akpugo)"
        verbose_name_plural = "Position (Akpugo)"


class Executive_Akpugo(models.Model):
    position = models.ForeignKey(Position_Akpugo, null=True, related_name='position_akpugo', on_delete=models.CASCADE)
    member = models.ForeignKey(Profile_Akpugo, null=True, related_name='member_akpugo', on_delete=models.CASCADE)
    today = datetime.date.today().year
    firstyear = 1999
    sessions = []
    while True:
        sessions.append((f'{firstyear}/' + str(firstyear + 1), f'{firstyear}/' + str(firstyear + 1)))
        if firstyear == today:
            break
        firstyear += 1
    session = models.CharField(choices=tuple(sessions), blank=True, verbose_name='Session', max_length=10000)

    def __str__(self):
        return f'{self.member.firstname} {self.member.lastname}'

    class Meta:
        verbose_name = "Executive (Akpugo)"
        verbose_name_plural = "Executives (Akpugo)"


class Profile_Okija(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, )
    firstname = models.CharField(verbose_name='First Name', max_length=255)
    lastname = models.CharField(verbose_name='Last Name', max_length=255)
    g = (('Male', 'Male'),
         ('Female', 'Female'),)
    gender = models.CharField(choices=g, default='Male', verbose_name='Gender', max_length=255)
    phone_num = models.CharField(verbose_name='Phone number', max_length=255, blank=True)
    department = models.CharField(default='none', verbose_name='Department', max_length=255)

    p = (('Soprano', 'Soprano'),
         ('Alto', 'Alto'),
         ('Tenor', 'Tenor'),
         ('Bass', 'Bass'),
         ('None', 'None'),)
    part = models.CharField(choices=p, help_text='The part of the person', max_length=100)
    c = (('Okija', 'Okija'),
         ('None', 'None'),)
    campus = models.CharField(choices=c, default='Okija', max_length=255)
    s = (('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'),
         ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'),
         ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'),
         ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'),
         ('Ekiti State', 'Ekiti State'),
         ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'),
         ('Jigawa State', 'Jigawa State'),
         ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kebbi State', 'Kebbi State'),
         ('Kogi State', 'Kogi State'),
         ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'),
         ('Niger State', 'Niger State'),
         ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'),
         ('Oyo State', 'Oyo State'),
         ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'),
         ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State'),
         )
    state = models.CharField(choices=s, verbose_name='State', max_length=255, blank=True)
    m = (('Single', 'Single'),
         ('Married', 'Married'),
         ('Religious', 'Religious'),
         )
    marital_status = models.CharField(choices=m, verbose_name='Marital Status', max_length=255, blank=True)
    birthday = models.DateField(default='1999-01-01', verbose_name='Birth Day', null=True, blank=True)
    joindate = models.DateField(default='1999-01-01', verbose_name='Join Date', null=True, blank=True)
    graduatedate = models.DateField(default='1999-01-01', verbose_name='Graduate Date', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.firstname} {self.lastname})"

    class Meta:
        verbose_name = "Profile (Okija)"
        verbose_name_plural = "Profile (Okija)"


class Position_Okija(models.Model):
    campus = models.CharField(default='Okija', max_length=255, editable=False)
    pos = models.CharField(verbose_name='Position', help_text='Enter the position in full', max_length=255)

    def __str__(self):
        return f'{self.pos} (Okija)'

    class Meta:
        verbose_name = "Position (Okija)"
        verbose_name_plural = "Position (Okija)"


class Executive_Okija(models.Model):
    position = models.ForeignKey(Position_Okija, null=True, related_name='position_okija', on_delete=models.CASCADE)
    member = models.ForeignKey(Profile_Okija, null=True, related_name='member_okija', on_delete=models.CASCADE)
    today = datetime.date.today().year
    firstyear = 1999
    sessions = []
    while True:
        sessions.append((f'{firstyear}/' + str(firstyear + 1), f'{firstyear}/' + str(firstyear + 1)))
        if firstyear == today:
            break
        firstyear += 1
    session = models.CharField(choices=tuple(sessions), blank=True, verbose_name='Session', max_length=255)

    def __str__(self):
        return f'{self.member.profile.firstname} {self.member.profile.lastname}'

    class Meta:
        verbose_name = "Executive (Okija)"
        verbose_name_plural = "Executives (Okija)"


class Profile_Elele(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, )
    firstname = models.CharField(verbose_name='First Name', max_length=255)
    lastname = models.CharField(verbose_name='Last Name', max_length=255)
    g = (('Male', 'Male'),
         ('Female', 'Female'),)
    gender = models.CharField(choices=g, default='Male', verbose_name='Gender', max_length=255)
    phone_num = models.CharField(verbose_name='Phone number', max_length=255, blank=True)
    department = models.CharField(default='none', verbose_name='Department', max_length=255)

    p = (('Soprano', 'Soprano'),
         ('Alto', 'Alto'),
         ('Tenor', 'Tenor'),
         ('Bass', 'Bass'),
         ('None', 'None'),)
    part = models.CharField(choices=p, help_text='The part of the person', max_length=100)
    c = (('Elele', 'Elele'),
         ('None', 'None'),)
    campus = models.CharField(choices=c, default='Elele', max_length=255)
    s = (('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'),
         ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'),
         ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'),
         ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'),
         ('Ekiti State', 'Ekiti State'),
         ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'),
         ('Jigawa State', 'Jigawa State'),
         ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kebbi State', 'Kebbi State'),
         ('Kogi State', 'Kogi State'),
         ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'),
         ('Niger State', 'Niger State'),
         ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'),
         ('Oyo State', 'Oyo State'),
         ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'),
         ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State'),
         )
    state = models.CharField(choices=s, verbose_name='State', max_length=255, blank=True)
    m = (('Single', 'Single'),
         ('Married', 'Married'),
         ('Religious', 'Religious'),
         )
    marital_status = models.CharField(choices=m, verbose_name='Marital Status', max_length=255, blank=True)
    birthday = models.DateField(default='1999-01-01', verbose_name='Birth Day', null=True, blank=True)
    joindate = models.DateField(default='1999-01-01', verbose_name='Join Date', null=True, blank=True)
    graduatedate = models.DateField(default='1999-01-01', verbose_name='Graduate Date', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.firstname} {self.lastname})"

    class Meta:
        verbose_name = "Profile (Elele)"
        verbose_name_plural = "Profile (Elele)"


class Position_Elele(models.Model):
    campus = models.CharField(default='Elele', max_length=255, editable=False)
    pos = models.CharField(verbose_name='Position', help_text='Enter the position in full', max_length=255)

    def __str__(self):
        return f'{self.pos} (Elele)'

    class Meta:
        verbose_name = "Position (Elele)"
        verbose_name_plural = "Position (Elele)"


class Executive_Elele(models.Model):
    position = models.ForeignKey(Position_Elele, null=True, related_name='position_elele', on_delete=models.CASCADE)
    member = models.ForeignKey(Profile_Elele, null=True, related_name='member_elele', on_delete=models.CASCADE)
    today = datetime.date.today().year
    firstyear = 1999
    sessions = []
    while True:
        sessions.append((f'{firstyear}/' + str(firstyear + 1), f'{firstyear}/' + str(firstyear + 1)))
        if firstyear == today:
            break
        firstyear += 1
    session = models.CharField(choices=tuple(sessions), blank=True, verbose_name='Session', max_length=255)

    def __str__(self):
        return f'{self.member.firstname} {self.member.lastname}'

    class Meta:
        verbose_name = "Executive (Elele)"
        verbose_name_plural = "Executives (Elele)"


class Profile_National(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, )
    firstname = models.CharField(verbose_name='First Name', max_length=255)
    lastname = models.CharField(verbose_name='Last Name', max_length=255)
    g = (('Male', 'Male'),
         ('Female', 'Female'),)
    gender = models.CharField(choices=g, default='Male', verbose_name='Gender', max_length=255)
    phone_num = models.CharField(verbose_name='Phone number', max_length=255, blank=True)
    department = models.CharField(default='none', verbose_name='Department', max_length=255)

    p = (('Soprano', 'Soprano'),
         ('Alto', 'Alto'),
         ('Tenor', 'Tenor'),
         ('Bass', 'Bass'),
         ('None', 'None'),)
    part = models.CharField(choices=p, help_text='The part of the person', max_length=100)
    c = (('National', 'National'),
         ('None', 'None'),)
    campus = models.CharField(choices=c, default='National', max_length=255)
    s = (('Abia State', 'Abia State'), ('Adamawa State', 'Adamawa State'), ('Akwa Ibom State', 'Akwa Ibom State'),
         ('Anambra State', 'Anambra State'), ('Bauchi State', 'Bauchi State'), ('Bayelsa State', 'Bayelsa State'),
         ('Benue State', 'Benue State'), ('Borno State', 'Borno State'), ('Cross River State', 'Cross River State'),
         ('Delta State', 'Delta State'), ('Ebonyi State', 'Ebonyi State'), ('Edo State', 'Edo State'),
         ('Ekiti State', 'Ekiti State'),
         ('Enugu State', 'Enugu State'), ('Gombe State', 'Gombe State'), ('Imo State', 'Imo State'),
         ('Jigawa State', 'Jigawa State'),
         ('Kaduna State', 'Kaduna State'), ('Kano State', 'Kano State'), ('Kebbi State', 'Kebbi State'),
         ('Kogi State', 'Kogi State'),
         ('Kwara State', 'Kwara State'), ('Lagos State', 'Lagos State'), ('Nasarawa State', 'Nasarawa State'),
         ('Niger State', 'Niger State'),
         ('Ogun State', 'Ogun State'), ('Ondo State', 'Ondo State'), ('Osun State', 'Osun State'),
         ('Oyo State', 'Oyo State'),
         ('Plateau State', 'Plateau State'), ('Rivers State', 'Rivers State'), ('Sokoto State', 'Sokoto State'),
         ('Taraba State', 'Taraba State'), ('Yobe State', 'Yobe State'), ('Zamfara State', 'Zamfara State'),
         )
    state = models.CharField(choices=s, verbose_name='State', max_length=255, blank=True)
    m = (('Single', 'Single'),
         ('Married', 'Married'),
         ('Religious', 'Religious'),
         )
    marital_status = models.CharField(choices=m, verbose_name='Marital Status', max_length=255, blank=True)
    birthday = models.DateField(default='1999-01-01', verbose_name='Birth Day', null=True, blank=True)
    joindate = models.DateField(default='1999-01-01', verbose_name='Join Date', null=True, blank=True)
    graduatedate = models.DateField(default='1999-01-01', verbose_name='Graduate Date', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.firstname} {self.lastname})"

    class Meta:
        verbose_name = "Profile (National)"
        verbose_name_plural = "Profile (National)"


class Position_National(models.Model):
    campus = models.CharField(default='National', max_length=255, editable=False)
    pos = models.CharField(verbose_name='Position', help_text='Enter the position in full', max_length=255)

    def __str__(self):
        return f'{self.pos} (National)'

    class Meta:
        verbose_name = "Position (National)"
        verbose_name_plural = "Position (National)"


class Executive_National(models.Model):
    position = models.ForeignKey(Position_National, null=True, related_name='position_national',
                                 on_delete=models.CASCADE)
    member = models.ForeignKey(Profile_National, null=True, related_name='member_national', on_delete=models.CASCADE)
    today = datetime.date.today().year
    firstyear = 1999
    sessions = []
    while True:
        sessions.append((f'{firstyear}/' + str(firstyear + 1), f'{firstyear}/' + str(firstyear + 1)))
        if firstyear == today:
            break
        firstyear += 1
    session = models.CharField(choices=tuple(sessions), blank=True, verbose_name='Session', max_length=255)

    def __str__(self):
        return f'{self.member.firstname} {self.member.lastname}'

    class Meta:
        verbose_name = "Executive (National)"
        verbose_name_plural = "Executives (National)"
