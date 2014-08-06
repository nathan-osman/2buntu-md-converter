<em>[important]I've been to the land of elementary OS, if I remember correctly I download an ISO back when Jupiter came out, but that time I only ran it on a virtual machine. Now, I've been running it on top of my Ubuntu 12.04 Desktop (the software components) on bare metal... and I'm learning to love it ;). With that said, you could say, I'm a wee bit biased, but as always, I will try to be fair to any competition.[/important]</em>

[notice]<strong>Disclaimer:</strong>

This is <strong>not</strong> an anti-gnome rant - but rather just an examination of the current situation and a possible alternative. You be the judge of which is better.[/notice]

[caption id="" align="aligncenter" width="454" caption="About Switchboard 0.9"]<img src="http://i.imgur.com/3h56B.png" />[/caption]

At UDS-P, the idea of greater collaboration between the elementary and Ubuntu communities/developers was discussed. Not only does elementary have apps we could do with, but elementary has some of the <em><strong>ideas</strong></em> that we need, and we have some of the infrastructure and discipline (yes, I know that's a controversial statement. bite me.) that they need.

&nbsp;
<h2>What is Switchboard anyway?</h2>
<em><strong>Switchboard is described as a:</strong></em>
<blockquote>"Modular desktop settings hub"</blockquote>
So essentially then, it is a cup holder for system settings. According to Cassidy James, Community Manager for the <a href="http://elementaryos.org/" target="_blank">elementary OS</a>, <em>anything</em> <a href="https://plus.google.com/108901876667002638432/posts/Wwq66ELYMQP" target="_blank">can be embedded</a> in Switchboard. That includes the funky settings application MyUnity (which is written in GAMBAS, of all things), and Ubuntu One's new (and controversial) Qt interface. It does not control any settings directly itself, so it is lightweight and simple.

Written in Vala, Switchboard also (obviously) is a GTK+ application, and won't draw the usual barrage of (idiotic) condemnation for being written in or using something other than C and GTK+ ;) (fanatics I'm looking at you ?).
<h2>Aight, so what can Switchboard do for me?</h2>
Eh... you?

Anyways... all jokes aside, really, what can Switchboard do for Ubuntu, or for any other Linux OS? Let's take a look at the current situation. We're not going to look into KDE, XFCE, or Enlightenment, since we are dealing with what is shipped with Ubuntu proper. Also, in the case of Gnome, the system settings aren't really broken, it's just that there are some short comings.
<h3>C or a .desktop file, nothing more?</h3>
Pretty much. That's all you can put in Gnome's new Control Center. Now, this is fine, if you are Gnome itself, because you would only have to concern yourself with the settings relevant to Gnome, and not really have to care about third parties (even though you should care about 3rd parties, but that's another story for another post). Of course, the level of integration offered by the current Control Center is commendable. However, the restriction of only allowing hard-coded panels written in C is not very flexible especially when one considers that Ubuntu has a myriad of applications that could put their settings there, but can't be embedded because the developers don't code in C, or don't want to shock users with bad design.

You see, if a setting is not directly integrated into the Control Center's all-in approach, it has to go in via a .desktop file, and that basically means you'll end up with extra windows popping up that are not really connected to the Control Centre. An example of this is the Ubuntu One Control Panel. It has never been integrated, and now to make matters worse, it's written in Qt, and even less visually integrated than before.
<div class="mceTemp mceIEcenter">

[caption id="attachment_2697" align="aligncenter" width="700" caption="Y U NO INTEGRATE?!ONE!?!"]<a href="http://www.2buntu.com/wp-content/uploads/2012/03/Screenshot-from-2012-03-14-1301081.png">[image:Screenshot-from-2012-03-14-1301081.png]</a>[/caption]

</div>
This is also the case with Printer settings, MyUnity, and Language Support settings. Terrible!

Okay, not terrible, but we could be doing a lot better. One of the things that still bugs me on the Linux Desktop is the level of fragmentation even within individual desktop environments. Users should not have to know, or care, whether an application is written in C++ or Erlang, or whether it uses GTK, Qt or EFL - it should <strong>just work</strong> from the standpoint of the user. This is one of the things that has helped Macintosh to succeed where it has - among a market of users who to a large extent don't care what they're running.
<h3>Okay so, what difference does Switchboard make in the big picture?</h3>
<em>Glad, you, or I, asked.</em>

The benefit of using a "container" like Switchboard is that much of the apparent fragmentation can be done away with quite easily. When I used Pantheon, I found it pleasantly surprising just how much the system seems to be trying to hide the fact that its made from many little pieces. Truth be told, you can feel this way on just about any system - until you begin to dig deeper. The system settings make up a large part of a user's perception of the system. After figuring out how to use the system, the next thing most people want to know is how to change things. Let's see how this area of using the desktop can affect user perception:
<ul>
    <li>When everything appears to be tightly integrated, it gives the user a sense that of a stable environment. This is one area where Enlightenment can seem confusing, while KDE seems like a professional system, for example.</li>
    <li>Having to deal with multiple windows is distracting. Distraction leads to frustration. Frustration leads to dissatisfaction.</li>
    <li>No matter how fancy your desktop, if configuring it is confusing, users won't like it.</li>
</ul>
<h3>Not convinced. Show me the money.</h3>
[caption id="attachment_2700" align="aligncenter" width="664" caption="Hmm... they look the same?"]<a href="http://www.2buntu.com/wp-content/uploads/2012/03/Screenshot-from-2012-03-14-135605.png"><img src="http://www.2buntu.com/wp-content/uploads/2012/03/Screenshot-from-2012-03-14-135605-1024x577.png" /></a>[/caption]

On the surface, there isn't much of a difference, and unfortunately at this time, some of the features referred to cannot be demonstrated (because for example there is no Ubuntu One plug for Switchboard as yet (it's still in pre-release or "pre-gold standard" development). The two in this screenshot are so similar you probably wouldn't notice that you're dealing with completely different systems...

...and that's part of the benefit. Replacing Gnome-Control-Center with Switchboard would hardly make a splash (in terms of drawbacks). The biggest hurdle would probably be the ethical issue of using a non-gnome application, which would have a backlash because people would complain and gripe about how Ubuntu is always using things without giving back upstream and blablabla yada yada yada. Personally, I beg to differ.

Switchboard supports most of Gnome Control Center's panels/applets, and support for them is improving. This means that for example, there could be remixes of Ubuntu that use either one, and you wouldn't notice the difference. A Gnome Shell remix, as another example, wouldn't require under the hood changes to give a pretty stock Gnome Experience on top of Ubuntu, in terms of system settings integration, because the underlying components would be easy to change around at will.

With all this being said then, there really is nothing holding back Ubuntu from switching to Switchboard (no pun intended) in future releases, so long as Switchboard is feature complete by then and up to the task. It would just be another area where two communities reach across the table and shake hands, and who knows, Gnome might even be able to pick up this tech for themselves ;).

&nbsp;

<em>/rant off</em>
<em>Roland Taylor, signing out.</em>
