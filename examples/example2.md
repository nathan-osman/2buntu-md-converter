Folks,

I am your Linux Advocate, Dietrich T. Schmitz.

[caption id="attachment_2931" align="alignright" width="180" caption="Apple Flashback"]<a href="http:/a/2buntu.com/wp-content/uploads/2012/04/apple.jpeg">[image:apple.jpeg]</a>[/caption]

Perhaps, you have read the latest story about the growing <a title="PC World Apple Flashback Attack Story" href="http://www.pcworld.com/businesscenter/article/253403/mac_malware_outbreak_is_bigger_than_conficker.html#tk.rss_news" target="_blank">FlashBack</a> epidemic that attacks Apple OSX-based computers. The media is reporting that this scourge may exceed numbers seen with the <a title="Care for a Conficker?  They're Yummy!" href="http://en.wikipedia.org/wiki/Conficker" target="_blank">Conficker</a> attack on Windows PCs.

If you have Linux, you can do a few things which will keep 'bad things from happening', including the above types of exploits attacking your PC.

Let me be clear here. <strong>Linux can get infected</strong>. But, if you follow a few simple rules, it will never happen:
<ol>
    <li>Obtain your software from the <a title="Repository" href="http://en.wikipedia.org/wiki/Software_repository" target="_blank">GPG key-ring protected repository</a> (repo) for your <a title="Linux Distribution" href="http://en.wikipedia.org/wiki/Linux_distribution" target="_blank">Distribution</a> (Distro),</li>
    <li>If you must go outside your repo, be sure to check the executable with the site's MD5 or preferably SHA <a title="Checksum" href="http://en.wikipedia.org/wiki/Checksum" target="_blank">checksum</a>, and,</li>
    <li>Sandbox your browser App, whatever it is using <a title="Linux Security Modules (LSM)" href="http://en.wikipedia.org/wiki/Linux_security_modules" target="_blank">Linux Security Modules</a>, e.g., SELinux or <a title="Ubuntu AppArmor LSM" href="https://wiki.ubuntu.com/AppArmor" target="_blank">AppArmor</a></li>
</ol>
<em>Ubuntu Linux</em> comes equipped with /etc/apparmor.d/usr.bin.firefox profile, but is 'disabled' out of the box.
You can enable it by first removing the disabled link:
<strong>$sudo rm /etc/apparmor.d/disable/usr.bin.firefox</strong>

then, add the Firefox profile to AppArmor with:
<strong>$sudo apparmor_parser -a /etc/apparmor.d/usr.bin.firefox</strong>

Essentially, everything you do during your Firefox session will be checked by LSM AppArmor using the above enabled profile.<strong> Any exploit which attempts to spawn and escalate privilege level will be</strong> <strong>stopped cold</strong>.

Unlike Windows and Apple, there is no need to scramble on a 'Zero Day' announcement. Your Distro will patch any security vulnerability/exploit affected software application in days if not hours and automatically download to your system.

That's it!

You should be fine. Here's my AppArmor status report:
<pre>dietrich@AOD260:~$ sudo aa-status
[sudo] password for dietrich:
apparmor module is loaded.
14 profiles are loaded.
14 profiles are in enforce mode.
/sbin/dhclient
/usr/lib/NetworkManager/nm-dhcp-client.action
/usr/lib/connman/scripts/dhclient-script
/usr/lib/cups/backend/cups-pdf
/usr/lib/firefox/firefox{,*[^s][^h]}
/usr/lib/firefox/firefox{,*[^s][^h]}//browser_java
/usr/lib/firefox/firefox{,*[^s][^h]}//browser_openjdk
/usr/lib/firefox/firefox{,*[^s][^h]}//sanitized_helper
/usr/lib/telepathy/mission-control-5
/usr/lib/telepathy/telepathy-*
/usr/sbin/cupsd
/usr/sbin/mysqld-akonadi
/usr/sbin/mysqld-akonadi///usr/sbin/mysqld
/usr/sbin/tcpdump
0 profiles are in complain mode.
8 processes have profiles defined.
8 processes are in enforce mode.
/sbin/dhclient (1905)
/usr/lib/firefox/firefox{,*[^s][^h]} (2380)
/usr/lib/firefox/firefox{,*[^s][^h]} (2444)
/usr/lib/firefox/firefox{,*[^s][^h]} (2447)
/usr/lib/firefox/firefox{,*[^s][^h]} (2448)
/usr/lib/firefox/firefox{,*[^s][^h]} (2547)
/usr/lib/telepathy/mission-control-5 (2167)
/usr/sbin/cupsd (1198)
0 processes are in complain mode.
0 processes are unconfined but have a profile defined.
dietrich@AOD260:~$</pre>
Linux with LSM: The safest operating system on the Planet.

I stake my reputation on it.

Dietrich T. Schmitz

Linux Advocate, Human Being
