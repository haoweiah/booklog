### gitbook新版本"gitbook build"命令导出的html不能跳转的解决办法



​		gitbook是一个很好用的工具，但是呢，我装了好几个版本，老是出现这个问题，于是请教周围的前端大神，大神提出了解决方法，这个问题倒是可以暂时解决，具体一劳永逸的做法还没找到，谁知道了，别忘了告诉我一声啊！
可能原因

新版本的gitbook不支持了这个功能
具体原因

由于点击事件被js代码禁用，所以点击没有反应，但是如果右键，在新窗口/新标签页打开的话是可以跳转的
解决办法

找到js代码，并修改

    找到项目目录gitbook
    找到目录下的theme.js文件
    找到下面的代码
    将if(m)改成if(false)
    
    由于代码是压缩后的，会没有空格，搜索的时候可以直接搜索： if(m)for(n.handler&&



    if (m)
        for (n.handler && (i = n,
        n = i.handler,
        o = i.selector),
        o && de.find.matchesSelector(Ye, o),
        n.guid || (n.guid = de.guid++),
        (u = m.events) || (u = m.events = {}),
        (a = m.handle) || (a = m.handle = function(t) {
            return "undefined" != typeof de && de.event.triggered !== t.type ? de.event.dispatch.apply(e, arguments) : void 0
        }
        ),
        t = (t || "").match(qe) || [""],
        l = t.length; l--; )
            s = Ze.exec(t[l]) || [],
            h = g = s[1],
            d = (s[2] || "").split(".").sort(),
            h && (f = de.event.special[h] || {},
            h = (o ? f.delegateType : f.bindType) || h,
            f = de.event.special[h] || {},
            c = de.extend({
                type: h,
                origType: g,
                data: r,
                handler: n,
                guid: n.guid,
                selector: o,
                needsContext: o && de.expr.match.needsContext.test(o),
                namespace: d.join(".")
            }, i),
            (p = u[h]) || (p = u[h] = [],
            p.delegateCount = 0,
            f.setup && f.setup.call(e, r, d, a) !== !1 || e.addEventListener && e.addEventListener(h, a)),
            f.add && (f.add.call(e, c),
            c.handler.guid || (c.handler.guid = n.guid)),
            o ? p.splice(p.delegateCount++, 0, c) : p.push(c),
            de.event.global[h] = !0)
        }

完成修改

保存，测试可用
————————————————
版权声明：本文为CSDN博主「七彩吞天蟒」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_42057852/article/details/81776917