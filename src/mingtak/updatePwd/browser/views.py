# -*- coding: utf-8 -*-

from mingtak.updatePwd import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from zope.interface import Interface
from plone.directives import form
from zope import schema
from z3c.form import button
from Products.statusmessages.interfaces import IStatusMessage


class IUpdatePasswordSelf(form.Schema):

    newPassword = schema.TextLine(
        title=_(u"New Password"),
    )


class UpdatePasswordSelf(form.SchemaForm):

    schema = IUpdatePasswordSelf
    ignoreContext = True

    label = _(u"Update Password")
    description = _(u"Please new password, update it.")


    @button.buttonAndHandler(_(u'Setup'))
    def handleApply(self, action):
        request = self.request
        response = request.response
        portal = api.portal.get()
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        newPassword = self.request.form['form.widgets.newPassword']
        user = api.user.get_current()
        accountid = user.id
        if user:
            user.setSecurityProfile(password=newPassword)
            message = _(u"Already update password!")
            mType = 'info'
        else:
            message = _(u"User not found!")
            mType = 'warning'

        response.redirect(portal.absolute_url())
        api.portal.show_message(message=message, request=request, type=mType)
        return

    @button.buttonAndHandler(_(u"Cancel"))
    def handleCancel(self, action):

        request = self.request
        response = request.response
        portal = api.portal.get()
        response.redirect(portal.absolute_url())
        message = _(u"Cancel this action!")
        api.portal.show_message(message=message, request=request, type='info')
        return


class IUpdatePassword(form.Schema):

    accountId = schema.TextLine(
        title=_(u"Account Id"),
    )

    newPassword = schema.TextLine(
        title=_(u"New Password"),
    )


class UpdatePassword(form.SchemaForm):

    schema = IUpdatePassword
    ignoreContext = True

    label = _(u"Update Password")
    description = _(u"Please input account id and password, update it.")


    @button.buttonAndHandler(_(u'Setup'))
    def handleApply(self, action):
        request = self.request
        response = request.response
        portal = api.portal.get()
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        accountId = self.request.form['form.widgets.accountId']
        newPassword = self.request.form['form.widgets.newPassword']
        user = api.user.get(username=accountId)
        if user:
            user.setSecurityProfile(password=newPassword)
            message = _(u"Already update password!")
            mType = 'info'
        else:
            message = _(u"User not found!")
            mType = 'warning'

        response.redirect('%s/@@update_password' % portal.absolute_url())
        api.portal.show_message(message=message, request=request, type=mType)
        return

    @button.buttonAndHandler(_(u"Cancel"))
    def handleCancel(self, action):

        request = self.request
        response = request.response
        portal = api.portal.get()
        response.redirect('%s/@@update_password' % portal.absolute_url())
        message = _(u"Cancel this action!")
        api.portal.show_message(message=message, request=request, type='info')
        return
