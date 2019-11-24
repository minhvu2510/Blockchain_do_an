;return null!==this.user.email&&""!==this.user.email&&e.push({icon:"icon-mail",text:t("settings","Resend welcome emails"),action:this.sendWelcomeMail}),e.concat(this.externalActions)},userGroups:function(){var e=this,t=this.groups.filter(function(t){return e.user.groups.includes(t.id)})

    a=a.filter(function(e){
        return-1===["admin","disabled"].indexOf(e.id)}),
    o&&o.text&&(o.text=t("settings","Admins"),o.icon="icon-user-admin",a.unshift(o))&&o.text&&(o.text=t("settings","Add group"),o.icon="icon-add",a.unshift(o)),
    u&&u.text&&(u.text=t("settings","Disabled users"),u.icon="icon-disabled-users",u.utils&&(u.utils.counter>0||-1===u.utils.counter)&&a.unshift(u));
var l={id:"everyone",key:"everyone",icon:"icon-contacts-dark",router:{name:"users"},text:t("settings","Everyone")};this.userCount>0&&r.a.set(l,"utils",{counter:this.userCount}),a.unshift(l);var d={id:"addgroup",key:"addgroup",icon:"icon-add",text:t("settings","Add group"),classes:this.loadingAddGroup?"icon-loading-small":""}

d={id:"addgroup",key:"addgroup",icon:"icon-add",text:t("settings","Add group")