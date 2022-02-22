# Opportunity Hack 2021
👉 www.ohack.org/hackathon
- DevPost Project: https://devpost.com/software/control-alt-delete

## Control Alt Delete - The Game

The game Control Alt Delete is named after a nonprofit organization called [Control Alt Delete](https://dvcontrolaltdelete.org/), which helps people escape domestic violence. This social impact game is designed to raise social awareness and inspire people to donate to the organization through interactive storytelling by putting the player in the shoes of someone trying to reset their life.

This web-based game raises awareness about:
* the cost of leaving an abusive relationship
* being prepared to leave
* safety
* online privacy concerns

## Problem Statement

Like many nonprofits, [Control Alt Delete](https://dvcontrolaltdelete.org/) struggles to illustrate how a donation supports their mission of helping women to escape domestic violence. The anonymity that Control Alt Delete maintains is necessary, but hurts their ability to collect grant funding which shifts their focus to fundraising to support their cause. If they are able to make donations more tangible to donors through their website, social media, and even augmented reality, the hope is that they can increase the people they can support through increased donations.

💰Requirements - Tangible Donations

Ultimately, the organization is looking for ways to increase donations. The following guidelines were provided:

* Consider mobile, website, and social media innovations
* Add tangibility for donations - even the smallest amount of donations matter
* Create a way to gather some metrics around engagement of users to better understand how many people are using this solution
* Consider gamification as a method to increase the marketing footprint organically.

## Design Thinking / Inspiration

The organization's donation mechanism does not deter people from donating as much as the challenge of raising visibility about this issue and encouraging people to donate to help address the issue.

```ruby

The issue is:

99% of all clients are financially abused. We help with one time assistance with rent/utility/move in payments allowing the women we help to remain housed during this transition to independence. 

These Survivors have needed financial and logistical help as they take control of their finances and futures.

```

This is why we focused on considering gamification as a way to introduce people to an issue that people shun away from because domestic violence predominately attracts negative news. Introducing people to the issue doesn't necessarily lead to a donation unless there is something "tangible" like a feel-good story that they leave with. 

So how can Control Alt Delete stand out from the crowd of other organiztaions with similar missions? 

Sometimes, novelty works. Since few nonprofit organizations use visual novels as a marketing tool, we went this route. Not only is it not used often in the nonprofit world, it also:

* attracts a built-in audience, with people of all ages who like interactive stories and gaming
* lets people experience the journey of some of the survivors Control Alt Delete has helped to create an emotional connection with players, who may become potential donors
* can be built on an open source engine that is free for commercial use, so the game can be sold as well

## How we built it

We built this on Ren'Py, which is "a visual novel engine – used by thousands of creators from around the world – that helps you use words, images, and sounds to tell interactive stories that run on computers and mobile devices."

Ren'Py is open source and free for commercial use.

## Challenges we ran into

Designing a cohesive story where one event affects another was challenging. There was a lot of back and forth, in collaboration with our nonprofit partner as well, and only so much we can build with time and knowledge. It was the first time working with Ren'Py for all of us.

## Accomplishments that we're proud of

We created a full-fledged story and game! It can be published on itch.io or other sites today.

## What we learned

We learned a lot about what goes into game design, from the game engine we choose to develop on to how we present the story to how we might educate players during the game to how to add elements of surprise and randomization so that every game is going to be different. There will never be a rote set of instructions for how to win - because even with all that you have going for you, there's always a chance that you will lose. That's just life - and that's what we're also teaching.

## What's next for Control Alt Delete

We look forward to building on this story more with our nonprofit partner Control Alt Delete.

# Notes on Game Design 

## Image / Audio / Font Source

https://www.rawpixel.com/

https://pixabay.com/

https://unsplash.com/

https://fonts.google.com/

## Color Scheme

Menu accent red - #D10E33

Menu accent blue - #0099CC

-----

Story character yellow - #FFFF8F

Story character police blue - #3366CC

Story character doctor blue - #2A7FBA

Story character purple - #8D539A

-----

Story character dialogue accent red - #D10E33

### Quick Tips

    #### Choice Menu Options

    You can show all options, with options being active or inactive based on conditions by setting the following variables:
    
    * define config.menu_include_disabled = true
    * define gui.choice_button_text_insensitive_color = "#999"


    #### Audio Options


    Play music (loops automatically):

    queue music "music.mp3" fadeout 1.0


    Fade out music:

    stop music fadeout 1.0


    Play a sound:

    play sound audio/bgm_story_wakeUp.mp3"


    Mix configurations:

    play music "audio/bgm_story_wakeUp.mp3" fadein 1.0 volume 0.25 # music loops by default


    #### Change Background Image

    You can add a file (named either "bg story_bedroom.png" or "bg story_bedroom.jpg") to the
    images directory to show it. You also have transition options like fade, dissolve, pixellate, etc.

    scene bg story_bedroom
    with fade