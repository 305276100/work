# coding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class TClass(models.Model):
    class_id = models.CharField(primary_key=True, max_length=30)
    class_name = models.CharField(max_length=30)
    class_home = models.CharField(max_length=30)
    class_createtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_class'
        verbose_name_plural = '班级表'


class TClassTeacher(models.Model):
    class_id = models.CharField(primary_key=True, max_length=30)
    teacher_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 't_class_teacher'
        unique_together = (('class_id', 'teacher_id'),)


class TGroup(models.Model):
    group_id = models.CharField(primary_key=True, max_length=30)
    group_name = models.CharField(max_length=30)
    group_leader = models.CharField(max_length=30, blank=True, null=True)
    group_it_leader = models.CharField(max_length=30, blank=True, null=True)
    group_createtime = models.DateTimeField()
    class_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 't_group'
        verbose_name_plural = '小组表'


class TJob(models.Model):
    job_id = models.CharField(primary_key=True, max_length=30)
    job_name = models.CharField(max_length=30)
    job_info = models.CharField(max_length=255)
    job_createtime = models.DateTimeField()
    class_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 't_job'
        verbose_name_plural = '作业表'


class TStudent(models.Model):
    student_id = models.CharField(primary_key=True, max_length=30)
    student_name = models.CharField(max_length=30)
    student_pwd = models.CharField(max_length=30)
    class_id = models.CharField(max_length=30)
    group_id = models.CharField(max_length=30, blank=True, null=True)
    student_createtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_student'
        verbose_name_plural = '学生表'


class TSubject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 't_subject'
        verbose_name_plural = '作业提交表'


class TTeacher(models.Model):
    teacher_id = models.CharField(primary_key=True, max_length=30)
    teacher_name = models.CharField(max_length=30)
    teacher_subject_type = models.ForeignKey(TSubject, models.DO_NOTHING, db_column='teacher_subject_type')

    class Meta:
        managed = False
        db_table = 't_teacher'
        verbose_name_plural = '授课教师表'
