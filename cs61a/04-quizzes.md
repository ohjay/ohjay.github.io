---
layout: page
title: Quizzes
permalink: /cs61a/quizzes/
---

<p>
    Y'know, just some mental jumping jacks for you to do.
</p>

<hr />

<div>
    <table class="qz">
        <tr><th colspan="4">Spring 2016</th></tr>
        <tr>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz2.pdf">Quiz &#35;2</a></td>
            <td><a href="http://pythontutor.com/composingprograms.html#code=def+flip(pancake%29%3A%0A++++if+pancake+%3D%3D+'cakepan'%3A%0A++++++++return+'pancake'%0A++++elif+heat+!%3D+4%3A%0A++++++++return+'cakepan'%0A++++return+'flipped'%0A++++++++%0Adef+cook(pancake,+heat,+flip%29%3A%0A++++if+heat+//+10%3A%0A++++++++return+'burnt'%0A++++heat+%2B%3D+3%0A++++pancake+%3D+flip(pancake%29%0A++++%0A++++def+cook(pancake,+heat,+flip%29%3A%0A++++++++if+heat+%3E%3D+5%3A%0A++++++++++++return+'done'%0A++++++++heat+%2B%3D+1%0A++++++++pancake+%3D+flip(pancake%29%0A++++++++return+cook(pancake,+heat,+lambda+p%3A+flip(p%29%29%0A++++++++%0A++++return+cook(pancake,+heat,+lambda+p%3A+flip(p%29+%5C%0A++++++++++++if+heat+%25+2+%3D%3D+0+else+p%29%0A++++%0Apancake,+heat+%3D+'batter',+1%0Acook(pancake,+heat,+flip%29&mode=display&origin=composingprograms.js&cumulative=true&py=3&rawInputLstJSON=%5B%5D&curInstr=33">Solution</a></td>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz2.py">Python Script</a></td>
            <td>Environment Diagrams</td>
        </tr>
        <tr>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz5.pdf">Quiz &#35;5</a></td>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz5_sol.pdf">Solution</a></td>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz5.py">Python Script</a></td>
            <td>Trees / Recursion</td>
        </tr>
        <tr>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz6.pdf">Quiz &#35;6</a></td>
            <td><a href="http://pythontutor.com/composingprograms.html#code=def+red(orange,+yellow,+green%29%3A%0A++++def+blue(%29%3A%0A++++++++if+1+%3E+2%3A%0A++++++++++++nonlocal+orange+%23+this+does+get+executed%0A++++++++else%3A%0A++++++++++++nonlocal+yellow+%23+so+does+this!%0A++++++++%0A++++++++orange,+yellow+%3D+orange+%2B+yellow+*+3,+orange+*+4%0A++++++++green+%3D+lambda+indigo%3A+int(orange+**+0.5%29%0A++++++++%0A++++++++if+yellow+%3C+orange%3A%0A++++++++++++green+%3D+lambda+violet%3A+int(orange+**+2%29%0A++++++++%0A++++++++return+green(orange%29%0A++++return+blue%0A%0Agatsby+%3D+red(3,+2,+1%29(%29&mode=display&origin=composingprograms.js&cumulative=true&py=3&rawInputLstJSON=%5B%5D&curInstr=16">Solution</a></td>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz6.py">Python Script</a></td>
            <td>Nonlocality</td>
        </tr>
        <tr>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz7.pdf">Quiz &#35;7</a></td>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz7_sol.pdf">Solution</a></td>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz7.py">Python Script</a></td>
            <td>OOP / OO Trees</td>
        </tr>
        <tr>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz8.pdf">Quiz &#35;8</a></td>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz8_sol.pdf">Solution</a></td>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz8.scm">Scheme File</a></td>
            <td>Scheme</td>
        </tr>
        <tr>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz9.pdf">Quiz &#35;9</a></td>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz9_sol.pdf">Solution</a></td>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz9.scm">Scheme File</a></td>
            <td>Tail Calls / Interpreters</td>
        </tr>
        <tr>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz10.pdf">Quiz &#35;10</a></td>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz10_sol.pdf">Solution</a></td>
            <td><a href="http://owenjow.xyz/cs61a/sp16/quiz/quiz10.py">Python Script</a></td>
            <td>Generators</td>
        </tr>
    </table>
</div>
