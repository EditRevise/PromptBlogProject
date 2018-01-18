<div style="text-align:center">
<img alt="Prompt" src="https://prompt.com/static/erEditRevise/img/logo/prompt1_64px.png">

# Technical Hire Test Project

</div>

## Introduction and Overview

Congratulations on moving on to the next stage of our hiring process. As we mentioned during your phone screen, you'll be the first outside hire on our growing engineering team, and you'll leave a lasting mark on our development culture. This project is your opportunity to showcase what you'll bring to the table. We will review your code quality, testing technique, and eye for design, and then discuss your design decisions and possible augmentations with you over the phone.

You're going to be building a blog! We believe this project is simple enough to be doable in one to two hours, and has enough nuance for you to showcase your technical flair. We even set up a Django development environment for you—you won't need to do that at Prompt anytime soon. You're free to use any back-end you want, though. Keep reading to learn about the full set of technical requirements.

If you have another project that is of similar or greater scope that you'll allow us to review in lieu of creating this blog, we'd be happy to do so. However, **we expect that you did at least half the design (architecture and visual) and development work** and that you can explain the minutiae of your project to us. We will attribute all the work to you, so any problems in your teammates' work will be held against you.

## Website Specification

### Views

This is a simple blog. It only requires two pages: one that allows a user to create a post, and one that allows a user to view existing posts in newest-first order and comment on them. Visually, you might find it cleaner to show a list of post previews, and create a post detail view that shows the full content and allows users to comment. It would be nice to know the name of who posts and comments.

You don't need to worry about authentication or security on any pages. We'll assume our users are in no way adversarial. We might ask you what you'd change if this assumption were removed.

We will be taking your blog's look and feel into account when reviewing your work. This doesn't mean you need to spend hours designing (please don't), but it does mean we'd like your pages to look clean. You're welcome (and encouraged) to use any open-source framework you want to help with content presentation.

### Concepts

#### Post

A Post is a blog post created by a user. A user should be able to enter some text and their name, and then send the text to the world. Users viewing the Post should know when and by whom it was posted.

Posts do not need to be editable or deletable. They also do not need to support rich content—though this seems like a natural augmentation to discuss ;). It'd be great if line breaks were preserved, though. If there's anything we've learned at Prompt, it's that authors love their paragraphs. (It's not the only thing we've learned.)

#### Comment

A Comment is an "insightful" (we said users are non-adversarial, not smart!) remark left by a user **in response to a Post or another Comment**. Similarly to a Post, users should be able to enter some text and their name, and then send their comment to the world. Users viewing Comments should be able to see when and by whom they were posted. You may choose any deterministic order for displaying Comments. Comments might be infinitely nested; however, you only need to design for the use case where they are nested at most 10 layers deep.

Comments should be editable by anyone. You don't need to track when or by whom changes are made—remember, our users are benevolent.

## Technical Requirements

### Back-end

* You may use any server framework you want. We have provided an example [Django](https://www.djangoproject.com/) environment, but you're also welcome to use [Node](https://nodejs.org/en/) / [Express](https://expressjs.com/), [Ruby](https://www.ruby-lang.org/en/downloads/) on [Rails](http://rubyonrails.org/), or any other framework with which you're comfortable

* We suggest exposing an API for post creation and retrieval, and comment creation, retrieval, modification, and deletion

    * We expect you will adhere to the conventions of how you build your API, whether it's with REST, GraphQL, SOAP, or another pattern

    * We recommend sticking to REST. If you use Django, we recommend using [Django-Rest-Framework](http://www.django-rest-framework.org/) to speed up the API creation process so you can focus on user experience

    * As with the rest of your blog, don't worry about authentication in your API

* We suggest writing a few back-end tests. This is only an hour project, though—don't go too crazy!

### Front-end

* You **must** use a front-end JavaScript framework. We want to see how you write JavaScript. We suggest using [Vue](https://vuejs.org/), but you can also use [React](https://reactjs.org/), [Angular](https://angularjs.org/), [Ember](https://www.emberjs.com/), or any other framework with which you're comfortable

* Your webpage **must not** reload when a Comment is added, edited, or deleted. This means you'll need to use AJAX. For simplicity, you should assume there are never any HTTP errors on these AJAX calls

    * PSST: If you're using Django for the first time, [this doc on Django's CSRF tokens](https://docs.djangoproject.com/en/1.11/ref/csrf/#setting-the-token-on-the-ajax-request) may save you some troubleshooting time

* You don't need to do any complicated bundling or make a single-page app. We want to see how good you are at JavaScript, not how good you are at Webpack (In fact, we've already got a lovely Webpack setup with hot reload for Vue components!)

* Your website only needs to work in one modern desktop browser, and does not need to work well on mobile. We're more interested in your code than your media queries

    * Please tell us which browser you choose, and [be prepared to defend any decision besides Chrome](https://en.wikipedia.org/wiki/Usage_share_of_web_browsers)

## Augmentations

During your follow-up call with us, we'll ask you how to implement a few augmentations to your application with you, based on your background and interests. Think about the most important things to add.

**Good luck!**

[Click here to download the example repository for Django.](https://github.com/EditRevise/PromptBlogProject)
