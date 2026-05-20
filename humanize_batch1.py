#!/usr/bin/env python3
"""Humanize 8 SilverStrength blog articles - rewrite content text only, preserve HTML structure."""

import os
import re

BASE = "/home/omeo_urke/silverstrength/blog"

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def humanize_article(filepath, replacements):
    """Apply find-and-replace pairs to humanize an article's content section only."""
    content = read_file(filepath)
    
    # Find the content section boundaries using regex (handles any whitespace between tags)
    start_match = re.search(r'<section class="content">\s*<div class="container">', content)
    if not start_match:
        print(f"  WARNING: Could not find opening content section in {filepath}")
        return False
    content_start = start_match.end()
    
    # Find closing - look for </div></section> after the content start
    end_match = re.search(r'</div>\s*</section>', content[content_start:])
    if not end_match:
        print(f"  WARNING: Could not find closing content section in {filepath}")
        return False
    content_end = content_start + end_match.start()
    
    before = content[:content_start]
    content_section = content[content_start:content_end]
    after = content[content_end:]
    
    # Apply all replacements to the content section only
    for old_text, new_text in replacements:
        if old_text in content_section:
            content_section = content_section.replace(old_text, new_text)
        else:
            print(f"  WARNING: Could not find text in {filepath}")
            print(f"    Looking for: {old_text[:80]}...")
    
    # Reassemble
    new_content = before + content_section + after
    write_file(filepath, new_content)
    return True


# ============================================================
# ARTICLE 1: hydration-for-seniors.html
# ============================================================
print("=== Article 1: hydration-for-seniors.html ===")

hyd_replacements = [
    (
        '<p>Water is the most essential nutrient your body needs. Every cell, tissue, and organ depends on it to function properly. Yet as we age, staying hydrated becomes harder \u2014 and dehydration becomes one of the most common reasons seniors end up in the hospital.</p>',
        '<p>Water is the most essential nutrient your body needs. Every cell, tissue, and organ depends on it to work right. Yet as we age, staying hydrated gets harder. Dehydration is one of the most common reasons seniors end up in the hospital.</p>'
    ),
    (
        '<p><strong>Hydration for seniors</strong> is not just about drinking water. It is about understanding how your body\'s needs change after 65, recognizing the warning signs before they become serious, and building simple habits that keep you feeling your best every day.</p>',
        '<p><strong>Hydration for seniors</strong> isnt just about drinking water. Its about understanding how your body changes after 65. Its about spotting warning signs before they turn serious. And its about building simple habits that keep you feeling your best every day.</p>'
    ),
    (
        '<p>This guide covers why seniors are at higher risk, how much water you really need, easy ways to drink more, and what to watch for \u2014 because something as simple as a glass of water can make a world of difference in how you feel.</p>',
        '<p>A glass of water can make a world of difference in how you feel. Lets talk about why seniors are at higher risk, how much water you really need, easy ways to drink more, and what to watch for.</p>'
    ),
    (
        '<p>Many people think dehydration only happens during hot weather or after exercise. But for seniors, the risk is present every day. Several age-related changes make it harder to stay hydrated:</p>',
        '<p>Many people think dehydration only happens in hot weather or after exercise. But for seniors, the risk is there every single day. Heres why:</p>'
    ),
    (
        '<div class="tip-box">\n<strong>Key Insight:</strong> Do not rely on thirst to tell you when to drink. If you are 65 or older, schedule your water intake the same way you schedule meals or medications. Your body cannot signal thirst as clearly as it used to.\n</div>',
        '<div class="tip-box">\n<strong>Key Insight:</strong> Dont rely on thirst to tell you when to drink. If youre 65 or older, schedule your water intake the same way you schedule meals or medications. Your body cant signal thirst as clearly as it used to.\n</div>'
    ),
    (
        '<p>There is no single number that works for everyone. Your fluid needs depend on your activity level, the weather, your medications, and your overall health. However, a general guideline for seniors is:</p>',
        '<p>Theres no single number that works for everyone. Your fluid needs depend on your activity level, the weather, your medications, and your overall health. But heres a general guideline:</p>'
    ),
    (
        '<p>Remember that \"total fluid\" includes more than just plain water. These all count toward your daily intake:</p>',
        '<p>Remember, \"total fluid\" includes more than just plain water. These all count toward your daily intake:</p>'
    ),
    (
        '<p>Dehydration can sneak up quickly. The early signs are easy to miss, especially in seniors. Watch for these symptoms:</p>',
        '<p>Dehydration can sneak up on you fast. The early signs are easy to miss, especially in seniors. Pay attention to these:</p>'
    ),
    (
        '<p>If you or a loved one experience sudden confusion, severe dizziness, or inability to keep fluids down, seek medical help right away.</p>',
        '<p>If you or a loved one experience sudden confusion, severe dizziness, or cant keep fluids down, get medical help right away.</p>'
    ),
    (
        '<p>Staying hydrated does not have to be complicated. These small changes make it easier to get enough fluids every day:</p>',
        '<p>Staying hydrated doesnt have to be complicated. Small changes make it easier to get enough fluids every day.</p>'
    ),
    (
        '<p>Place a water bottle or full glass on your bedside table, next to your favorite chair, and in the kitchen. When water is visible and easy to reach, you will drink more without thinking about it.</p>',
        '<p>Place a water bottle or full glass on your bedside table, next to your favorite chair, and in the kitchen. When water is visible and easy to reach, youll drink more without thinking about it.</p>'
    ),
    (
        '<p>Drink a glass of water at specific times each day \u2014 when you wake up, with each meal, before bed, and every time you take a medication. Routine makes hydration automatic.</p>',
        '<p>Drink a glass of water at set times each day. When you wake up, with each meal, before bed, and every time you take medication. Routine makes hydration automatic.</p>'
    ),
    (
        '<p>If plain water feels boring, add a slice of lemon, lime, cucumber, or a few berries. Herbal teas (hot or iced) are also excellent hydrating options with natural flavor variety.</p>',
        '<p>If plain water feels boring, add a slice of lemon, lime, cucumber, or a few berries. Herbal teas, hot or iced, are also excellent hydrating options with natural flavor.</p>'
    ),
    (
        '<p>Many fruits and vegetables are 90% water or more. Watermelon, cantaloupe, cucumbers, tomatoes, celery, strawberries, and oranges are excellent choices. A fruit salad or vegetable soup is as hydrating as a glass of water.</p>',
        '<p>Many fruits and vegetables are 90% water or more. Watermelon, cantaloupe, cucumbers, tomatoes, celery, strawberries, and oranges are all great choices. A fruit salad or vegetable soup is as hydrating as a glass of water.</p>'
    ),
    (
        '<p>A clear water bottle with time markings (8 AM, 10 AM, 12 PM, etc.) helps you pace your intake throughout the day. It turns hydration into a simple visual goal.</p>',
        '<p>A clear water bottle with time markings, like 8 AM, 10 AM, 12 PM, helps you pace your intake. It turns hydration into a simple visual goal.</p>'
    ),
    (
        '<p>Link drinking water to habits you already have. Every time you brush your teeth, take a few sips. Every time you sit down to watch TV, keep water nearby. When you take medication, drink a full glass of water \u2014 not just a sip.</p>',
        '<p>Link drinking water to habits you already have. Every time you brush your teeth, take a few sips. Every time you sit down to watch TV, keep water nearby. When you take medication, drink a full glass of water, not just a sip.</p>'
    ),
    (
        '<div class="tip-box">\n<strong>Senior Tip:</strong> If you worry about frequent bathroom trips at night, front-load your hydration earlier in the day. Drink most of your water before 6 PM, and only take small sips in the evening. Your body will thank you with better sleep. For more on restful sleep, read our <a href="/blog/sleep-tips-seniors.html">sleep tips for seniors</a>.\n</div>',
        '<div class="tip-box">\n<strong>Senior Tip:</strong> If you worry about frequent bathroom trips at night, front-load your hydration earlier in the day. Drink most of your water before 6 PM and only take small sips in the evening. Your body will thank you with better sleep. For more on restful sleep, read our <a href="/blog/sleep-tips-seniors.html">sleep tips for seniors</a>.\n</div>'
    ),
    (
        '<p>If you are active \u2014 walking, doing resistance band exercises, or practicing balance drills \u2014 your need for water increases. Even mild exercise causes fluid loss through sweat, and seniors often do not feel as thirsty after activity as younger adults do.</p>',
        '<p>If youre active, walking, using resistance bands, or practicing balance drills, your need for water goes up. Even mild exercise causes fluid loss through sweat. And seniors often dont feel as thirsty after activity as younger adults do.</p>'
    ),
    (
        '<p>Many common medications affect hydration. Here is what to watch for:</p>',
        '<p>Many common medications affect hydration. Heres what to watch for:</p>'
    ),
    (
        '<p>A: Most seniors should aim for 6\u20138 cups (48\u201364 ounces) of total fluid per day. This includes water, herbal tea, milk, and water-rich foods. Your needs may vary based on activity, medications, and health conditions \u2014 ask your doctor for a personalized recommendation.</p>',
        '<p>A: Most seniors should aim for 6-8 cups of total fluid per day. This includes water, herbal tea, milk, and water-rich foods. Your needs may vary based on activity, medications, and health conditions. Ask your doctor for a personalized recommendation.</p>'
    ),
    (
        '<p>A: The sense of thirst becomes less reliable with age. Kidneys become less efficient at conserving water, medications increase fluid loss, and mobility challenges can make it harder to get water regularly.</p>',
        '<p>A: Your sense of thirst becomes less reliable with age. Your kidneys become less efficient at conserving water. Medications can increase fluid loss. And mobility challenges can make it harder to get water regularly.</p>'
    ),
    (
        '<p>A: Dry mouth, fatigue, dizziness, confusion, dark urine, infrequent urination, headaches, and muscle cramps. In seniors, confusion is often one of the earliest signs \u2014 do not ignore it.</p>',
        '<p>A: Dry mouth, fatigue, dizziness, confusion, dark urine, infrequent urination, headaches, and muscle cramps. In seniors, confusion is often one of the earliest signs. Dont ignore it.</p>'
    ),
    (
        '<p>A: Yes. Moderate amounts of coffee and tea (up to 3 cups per day) count toward your fluid intake. The mild diuretic effect of caffeine does not cancel out the hydrating benefit of the beverage itself.</p>',
        '<p>A: Yes. Moderate amounts of coffee and tea, up to 3 cups per day, count toward your fluid intake. The mild diuretic effect of caffeine doesnt cancel out the hydrating benefit of the beverage itself.</p>'
    ),
    (
        '<p>Hydration is one of the simplest, most powerful things you can do for your health. It boosts energy, sharpens your mind, protects your kidneys, and helps every system in your body work better. And it does not require expensive supplements or complicated routines \u2014 just water, a little awareness, and consistent daily habits.</p>',
        '<p>Hydration is one of the simplest, most powerful things you can do for your health. It boosts your energy, sharpens your mind, protects your kidneys, and helps every system in your body work better. All it takes is water, a little awareness, and consistent daily habits.</p>'
    ),
    (
        '<p>Start with one small change today: place a glass of water next to your bed tonight. Tomorrow morning, drink it first thing. That one change, repeated daily, can transform how you feel.</p>',
        '<p>Start with one small change today. Place a glass of water next to your bed tonight. Tomorrow morning, drink it first thing. That one change, repeated daily, can transform how you feel.</p>'
    ),
]

f = os.path.join(BASE, "hydration-for-seniors.html")
result = humanize_article(f, hyd_replacements)
print(f"  Result: {'OK' if result else 'FAILED'}")

# ============================================================
# ARTICLE 2: balance-exercises-seniors.html
# ============================================================
print("=== Article 2: balance-exercises-seniors.html ===")

bal_replacements = [
    (
        '<p>Losing your balance can be frightening. One moment you are standing, and the next you are reaching for a wall, a counter, or worse \u2014 falling. For seniors 65 and older, falls are the leading cause of injury. But here is the good news: <strong>balance is a skill you can improve</strong>, just like strength or flexibility. And it does not take hours at the gym.</p>',
        '<p>Losing your balance can be frightening. One moment youre standing, and the next youre reaching for a wall, a counter, or worse, falling. For seniors 65 and older, falls are the leading cause of injury. But heres the good news: <strong>balance is a skill you can improve</strong>, just like strength or flexibility. And it doesnt take hours at the gym.</p>'
    ),
    (
        '<p>Balance exercises for seniors are simple, safe, and highly effective. With just a few minutes of practice each day, you can strengthen the muscles and reflexes that keep you steady on your feet. This guide walks you through five proven balance drills you can do at home, explains why balance declines with age, and shows you how to build a daily routine that fits your life.</p>',
        '<p>Balance exercises for seniors are simple, safe, and highly effective. With just a few minutes of practice each day, you can strengthen the muscles and reflexes that keep you steady on your feet. We walk through five proven balance drills you can do at home, explain why balance declines with age, and show you how to build a daily routine that fits your life.</p>'
    ),
    (
        '<p>Balance is not something you are born with \u2014 it is a complex system involving your eyes, inner ears, muscles, and brain. As we age, several things happen that can throw this system off:</p>',
        '<p>Balance isnt something youre born with. Its a complex system involving your eyes, inner ears, muscles, and brain. As we age, several things can throw this system off:</p>'
    ),
    (
        '<p>The key insight is this: <strong>balance training directly counteracts every one of these changes</strong>. You can rebuild strength, retrain your reflexes, and improve your body\'s ability to stay upright \u2014 at any age.</p>',
        '<p>Heres the key: <strong>balance training directly counteracts every one of these changes</strong>. You can rebuild strength, retrain your reflexes, and improve your ability to stay upright at any age.</p>'
    ),
    (
        '<div class="tip-box">\n<strong>Safety first</strong> \u2014 Always have a sturdy chair, countertop, or wall within arm\'s reach when doing balance exercises. Wear supportive, non-slip shoes or go barefoot on a non-slip surface. If you feel dizzy or unsteady, stop and sit down. Never push through pain or fear.\n</div>',
        '<div class="tip-box">\n<strong>Safety first</strong>. Always have a sturdy chair, countertop, or wall within arms reach when doing balance exercises. Wear supportive, non-slip shoes or go barefoot on a non-slip surface. If you feel dizzy or unsteady, stop and sit down. Never push through pain or fear.\n</div>'
    ),
    (
        '<p>These five exercises progress from easiest to most challenging. Start with number one and only move to the next when you feel completely comfortable. There is no race \u2014 <strong>progress at your own pace</strong>.</p>',
        '<p>These five exercises go from easiest to most challenging. Start with number one and only move to the next when you feel completely comfortable. Theres no race. <strong>Progress at your own pace</strong>.</p>'
    ),
    (
        '<p>Consistency is the secret to better balance. Here is a simple daily plan:</p>',
        '<p>Consistency is the secret to better balance. Heres a simple daily plan:</p>'
    ),
    (
        '<p>Do your balance routine at the same time each day \u2014 after breakfast, before lunch, or during a commercial break while watching television. <strong>Building a habit is more important than building intensity</strong>. A 5-minute daily practice beats a 30-minute session once a week every time.</p>',
        '<p>Do your balance routine at the same time each day. After breakfast, before lunch, or during a commercial break while watching TV. <strong>Building a habit is more important than building intensity</strong>. A 5-minute daily practice beats a 30-minute session once a week every time.</p>'
    ),
    (
        '<p>These small improvements add up to a <strong>dramatically lower risk of falling</strong>. According to the <a href="https://www.cdc.gov/falls/data-research/index.html" target="_blank" rel="noopener">Centers for Disease Control and Prevention</a>, balance training combined with strength exercises can reduce fall risk by up to 50 percent. That is a powerful return on a 10-minute daily investment.</p>',
        '<p>These small improvements add up to a <strong>dramatically lower risk of falling</strong>. According to the <a href="https://www.cdc.gov/falls/data-research/index.html" target="_blank" rel="noopener">Centers for Disease Control and Prevention</a>, balance training combined with strength exercises can reduce fall risk by up to 50 percent. Thats a powerful return on a 10-minute daily investment.</p>'
    ),
    (
        '<p>A: Aim for daily practice, even if it is just 5 minutes. Consistency matters more than duration. Most seniors see noticeable improvement in stability within 2 to 4 weeks of daily practice.</p>',
        '<p>A: Aim for daily practice, even if its just 5 minutes. Consistency matters more than duration. Most seniors see noticeable improvement in stability within 2 to 4 weeks of daily practice.</p>'
    ),
    (
        '<p>A: Yes. Research from the CDC shows that balance training reduces fall risk by 24 to 50 percent when done consistently. Balance exercises strengthen the muscles and neural pathways that keep you upright and responsive to shifts in your center of gravity.</p>',
        '<p>A: Yes. Research from the CDC shows that balance training reduces fall risk by 24 to 50 percent when done consistently. These exercises strengthen the muscles and neural pathways that keep you upright and responsive to shifts in your center of gravity.</p>'
    ),
    (
        '<p>A: No. Most balance exercises require nothing more than a sturdy chair for support and comfortable clothing. As you progress, you may add a countertop or wall for extra stability, but no special equipment is needed to start.</p>',
        '<p>A: No. Most balance exercises require nothing more than a sturdy chair for support and comfortable clothing. As you progress, you may use a countertop or wall for extra stability. But no special equipment is needed to start.</p>'
    ),
    (
        '<p>A: Start with exercises that keep both hands on a support surface. Use a sturdy chair or counter. Only progress to one-handed or no-handed support when you feel completely steady. If you ever feel unsafe, return to the supported version. Safety always comes first.</p>',
        '<p>A: Start with exercises that keep both hands on a support surface. Use a sturdy chair or counter. Only move to one-handed or no-handed support when you feel completely steady. If you ever feel unsafe, go back to the supported version. Safety always comes first.</p>'
    ),
    (
        '<p>A: Yes. Perform the exercises while holding your walker or cane for support. Focus on the movement patterns and muscle engagement. Over time, your stability may improve enough to reduce your reliance on walking aids, but always follow your doctor\'s guidance.</p>',
        '<p>A: Yes. Perform the exercises while holding your walker or cane for support. Focus on the movement patterns and muscle engagement. Over time, your stability may improve enough to reduce your reliance on walking aids. But always follow your doctors guidance.</p>'
    ),
    (
        '<p>You do not need special equipment, a gym membership, or hours of free time. You need a sturdy chair, 5 to 10 minutes a day, and the willingness to start where you are. Your balance will improve \u2014 not because you are trying hard, but because you are showing up consistently.</p>',
        '<p>You dont need special equipment, a gym membership, or hours of free time. You need a sturdy chair, 5 to 10 minutes a day, and the willingness to start where you are. Your balance will improve. Not because youre trying hard, but because youre showing up consistently.</p>'
    ),
    (
        '<p>Every time you practice, you are telling your body: <strong>I want to stay steady, independent, and active</strong>. And your body will respond. The first week might feel awkward. By week three, the movements will feel familiar. By week four, you will notice the difference in how you walk, stand, and move through your day.</p>',
        '<p>Every time you practice, youre telling your body: <strong>I want to stay steady, independent, and active</strong>. And your body will respond. The first week might feel awkward. By week three, the movements will feel familiar. By week four, youll notice the difference in how you walk, stand, and move through your day.</p>'
    ),
    (
        '<p>That is the power of balance training. It does not just prevent falls \u2014 it restores confidence. And confidence is what keeps you living the life you love.</p>',
        '<p>Thats the power of balance training. It doesnt just prevent falls. It restores confidence. And confidence is what keeps you living the life you love.</p>'
    ),
]

f = os.path.join(BASE, "balance-exercises-seniors.html")
result = humanize_article(f, bal_replacements)
print(f"  Result: {'OK' if result else 'FAILED'}")

# ============================================================
# ARTICLE 3: mobility-exercises-seniors.html
# ============================================================
print("=== Article 3: mobility-exercises-seniors.html ===")

mob_replacements = [
    (
        '<p>If you\'re over 65, maintaining your mobility isn\'t just about staying active \u2014 it\'s about preserving your freedom. The ability to get up from a chair, carry groceries, play with grandchildren, and move through your day without stiffness or pain is something no medication can replace.</p>',
        '<p>If youre over 65, maintaining your mobility isnt just about staying active. Its about preserving your freedom. The ability to get up from a chair, carry groceries, play with grandchildren, and move through your day without stiffness or pain. No medication can replace that.</p>'
    ),
    (
        '<p>The good news is that you don\'t need a gym membership or expensive equipment. These five mobility exercises are safe, gentle on the joints, and proven to help seniors maintain flexibility, balance, and strength well into their 80s and beyond. Let\'s get started.</p>',
        '<p>The good news is you dont need a gym membership or expensive equipment. These five mobility exercises are safe, gentle on the joints, and proven to help seniors maintain flexibility, balance, and strength well into their 80s and beyond.</p>'
    ),
    (
        '<div class="tip-box"><strong>Safety First:</strong> Always consult your healthcare provider before beginning any new exercise routine, especially if you have existing medical conditions, joint concerns, or recent injuries. Start slowly and listen to your body \u2014 discomfort is a signal to ease up, not push through.</div>',
        '<div class="tip-box"><strong>Safety First:</strong> Always check with your healthcare provider before starting any new exercise routine, especially if you have existing medical conditions, joint concerns, or recent injuries. Start slowly and listen to your body. Discomfort is a signal to ease up, not push through.</div>'
    ),
    (
        '<p>Consistency is far more important than intensity when it comes to mobility. Here is a simple weekly schedule that takes just 10-15 minutes per day:</p>',
        '<p>When it comes to mobility, consistency matters far more than intensity. Heres a simple weekly schedule that takes just 10-15 minutes per day:</p>'
    ),
    (
        '<p>Adjust this schedule based on how your body feels. If you\'re sore, take an extra rest day. If you feel great, add an extra set. The goal is to make mobility practice a lifelong habit, not a chore.</p>',
        '<p>Adjust this schedule based on how your body feels. If youre sore, take an extra rest day. If you feel great, add an extra set. The goal is to make mobility practice a lifelong habit, not a chore.</p>'
    ),
    (
        '<p>Aim for 10-15 minutes daily. Consistency matters more than intensity \u2014 even 5 minutes on busy days helps maintain flexibility and balance. Morning is often the best time because joints tend to be stiff after a night\'s sleep.</p>',
        '<p>Aim for 10-15 minutes daily. Consistency matters more than intensity. Even 5 minutes on busy days helps maintain flexibility and balance. Morning is often the best time because joints tend to be stiff after a nights sleep.</p>'
    ),
    (
        '<p>Yes, absolutely. Balance and mobility exercises are the most effective way to reduce fall risk in seniors 65+. They strengthen the muscles and neural pathways that keep you steady on your feet. When combined with strength training, the fall prevention benefits are even greater.</p>',
        '<p>Yes, absolutely. Balance and mobility exercises are the most effective way to reduce fall risk in seniors 65+. They strengthen the muscles and neural pathways that keep you steady on your feet. When you add strength training, the benefits are even greater.</p>'
    ),
    (
        '<p>Most mobility exercises require no equipment at all. A sturdy chair with armrests is helpful for balance support. For comfort, consider a non-slip exercise mat. Keep a wall or counter nearby when practicing standing exercises. Resistance bands and balance cushions are optional additions as you progress.</p>',
        '<p>Most mobility exercises require no equipment at all. A sturdy chair with armrests is helpful for balance support. For comfort, consider a non-slip exercise mat. Keep a wall or counter nearby for standing exercises. Resistance bands and balance cushions are optional as you progress.</p>'
    ),
    (
        '<p>Mild muscle soreness, especially in the first week, is completely normal as your body adapts to new movements. However, sharp joint pain or soreness lasting more than 48 hours means you may be pushing too hard. Reduce intensity and consult your doctor if pain persists.</p>',
        '<p>Mild muscle soreness, especially in the first week, is normal as your body adapts to new movements. But sharp joint pain or soreness lasting more than 48 hours means you may be pushing too hard. Ease up and check with your doctor if pain continues.</p>'
    ),
    (
        '<p>Absolutely. Many exercises can be adapted for walker or cane users. Keep your mobility aid nearby for standing exercises. Seated exercises are ideal if standing for long periods is difficult. Always prioritize safety and stability over range of motion.</p>',
        '<p>Absolutely. Many exercises can be adapted for walker or cane users. Keep your mobility aid nearby for standing exercises. Seated exercises work well if standing for long periods is hard. Always put safety and stability first.</p>'
    ),
    (
        '<p>Your ability to move freely isn\'t something to take for granted \u2014 but it\'s never too late to improve it. These five exercises form a foundation that can keep you independent, active, and confident for years to come. Start with just one or two exercises today and build from there.</p>',
        '<p>Your ability to move freely isnt something to take for granted. But its never too late to improve it. These five exercises form a foundation that can keep you independent, active, and confident for years to come. Start with just one or two exercises today and build from there.</p>'
    ),
    (
        '<p>Having the right support tools can make your mobility practice safer and more effective. Here\'s what experienced seniors recommend:</p>',
        '<p>Having the right support tools can make your mobility practice safer and more effective. Heres what experienced seniors recommend:</p>'
    ),
]

f = os.path.join(BASE, "mobility-exercises-seniors.html")
result = humanize_article(f, mob_replacements)
print(f"  Result: {'OK' if result else 'FAILED'}")

# ============================================================
# ARTICLE 4: senior-strength-training-guide.html
# ============================================================
print("=== Article 4: senior-strength-training-guide.html ===")

str_replacements = [
    (
        '<p>Strength training isn\'t just for young athletes. After 65, it becomes one of the <strong>most important things you can do for your health and independence</strong>. Whether you want to carry groceries more easily, get up from a chair without using your hands, or reduce your risk of falls and fractures, building strength is the key.</p>',
        '<p>Strength training isnt just for young athletes. After 65, it becomes one of the <strong>most important things you can do for your health and independence</strong>. Whether you want to carry groceries more easily, get up from a chair without using your hands, or reduce your risk of falls and fractures, building strength is the key.</p>'
    ),
    (
        '<p>But with so many options \u2014 resistance bands, dumbbells, machines, bodyweight exercises \u2014 how do you choose the <strong>best strength training approach for your needs</strong>? This guide walks you through everything you need to know to start safely and effectively.</p>',
        '<p>But with so many options, resistance bands, dumbbells, machines, bodyweight exercises, how do you choose the <strong>best approach for your needs</strong>? We walk you through everything you need to know to start safely and effectively.</p>'
    ),
    (
        '<div class="tip-box"><strong>Before you begin:</strong> Always consult your doctor before starting a new exercise program, especially if you have chronic conditions, joint pain, or take medications that affect balance.</div>',
        '<div class="tip-box"><strong>Before you begin:</strong> Always check with your doctor before starting a new exercise program, especially if you have chronic conditions, joint pain, or take medications that affect balance.</div>'
    ),
    (
        '<p>Here\'s what consistent strength training does for seniors:</p>',
        '<p>Heres what consistent strength training does for seniors:</p>'
    ),
    (
        '<p>Not all strength training methods are created equal for older adults. Here\'s how the most popular options compare so you can choose what works best <strong>for your body and goals</strong>.</p>',
        '<p>Not all strength training methods work the same for older adults. Heres how the most popular options compare, so you can choose what works best <strong>for your body and goals</strong>.</p>'
    ),
    (
        '<p>Choosing the right equipment is crucial for safety and effectiveness. Here\'s our buying guide for senior strength training gear.</p>',
        '<p>Choosing the right equipment matters for safety and effectiveness. Heres our buying guide for senior strength training gear.</p>'
    ),
    (
        '<p>Following these safety rules will help you <strong>train effectively while avoiding injury</strong>.</p>',
        '<p>Follow these safety rules to <strong>train effectively while avoiding injury</strong>.</p>'
    ),
    (
        '<p>Experts recommend <strong>2-3 strength training sessions per week</strong> with at least 48 hours of rest between sessions targeting the same muscle groups. This gives your muscles time to recover and grow stronger.</p>',
        '<p>Experts recommend <strong>2-3 strength training sessions per week</strong> with at least 48 hours of rest between sessions for the same muscle groups. This gives your muscles time to recover and grow stronger.</p>'
    ),
    (
        '<p><strong>Resistance bands are the safest option for beginners</strong> because they provide gentle, controlled resistance that is easy on joints. Light dumbbells (1-5 lbs to start) and bodyweight exercises are also excellent choices. Always start light and focus on proper form.</p>',
        '<p><strong>Resistance bands are the safest option for beginners</strong> because they provide gentle, controlled resistance that is easy on joints. Light dumbbells, 1-5 lbs to start, and bodyweight exercises are also excellent choices. Always start light and focus on proper form.</p>'
    ),
    (
        '<p>Most seniors notice <strong>improved strength and mobility within 4-6 weeks</strong> of consistent training. Visible muscle changes typically appear after 8-12 weeks. Many report feeling stronger and more energetic within the first two weeks.</p>',
        '<p>Most seniors notice <strong>improved strength and mobility within 4-6 weeks</strong> of consistent training. Visible muscle changes usually appear after 8-12 weeks. Many report feeling stronger and more energetic within the first two weeks.</p>'
    ),
    (
        '<p><strong>Yes.</strong> Always consult your healthcare provider before beginning any new exercise program, especially if you have chronic conditions, joint issues, or take medications that affect balance or heart rate. Your doctor can help you determine safe starting weights and exercise modifications.</p>',
        '<p><strong>Yes.</strong> Always check with your healthcare provider before starting any new exercise program, especially if you have chronic conditions, joint issues, or take medications that affect balance or heart rate. Your doctor can help you determine safe starting weights and exercise modifications.</p>'
    ),
    (
        '<p>Strength training after 65 is one of the <strong>smartest investments you can make in your health and independence</strong>. You don\'t need expensive equipment or a gym membership to start. A pair of resistance bands and a sturdy chair are enough to begin building muscle, improving bone density, and protecting your mobility for years to come.</p>',
        '<p>Strength training after 65 is one of the <strong>smartest investments you can make in your health and independence</strong>. You dont need expensive equipment or a gym membership to start. A pair of resistance bands and a sturdy chair are enough to begin building muscle, improving bone density, and protecting your mobility for years to come.</p>'
    ),
    (
        '<p>Start with one or two exercises from the routine above, focus on proper form, and gradually build up. Your future self will thank you.</p>',
        '<p>Start with one or two exercises from the routine above. Focus on proper form and gradually build up. Your future self will thank you.</p>'
    ),
    (
        '<p><em>Disclaimer: This article is for informational purposes only and is not a substitute for professional medical advice. Always consult your doctor before starting any exercise program, especially if you have pre-existing health conditions or concerns.</em></p>',
        '<p><em>Disclaimer: This article is for informational purposes only and is not a substitute for professional medical advice. Always check with your doctor before starting any exercise program, especially if you have pre-existing health conditions or concerns.</em></p>'
    ),
]

f = os.path.join(BASE, "senior-strength-training-guide.html")
result = humanize_article(f, str_replacements)
print(f"  Result: {'OK' if result else 'FAILED'}")

# ============================================================
# ARTICLE 5: brain-games-seniors.html
# ============================================================
print("=== Article 5: brain-games-seniors.html ===")

brain_replacements = [
    (
        '<p>Have you ever walked into a room and forgotten why? Or struggled to recall a name you know perfectly well? These moments happen to all of us, and they can feel worrying. The good news is that your brain, like any muscle, responds to exercise. With the right mental activities, you can keep your mind sharp, improve your memory, and even lower your risk of cognitive decline.</p>',
        '<p>Have you ever walked into a room and forgotten why? Or struggled to recall a name you know perfectly well? These moments happen to all of us. And they can feel worrying. The good news is your brain, like any muscle, responds to exercise. With the right mental activities, you can keep your mind sharp, improve your memory, and even lower your risk of cognitive decline.</p>'
    ),
    (
        '<p><strong>Brain games and mental stimulation</strong> are simple, enjoyable ways to challenge your mind every day. They don\'t require a computer, a subscription, or any special skills \u2014 just a few minutes and a willingness to try something new. This guide covers the best brain exercises for seniors, how they work, and how to make them a fun part of your daily routine.</p>',
        '<p><strong>Brain games and mental stimulation</strong> are simple, enjoyable ways to challenge your mind every day. They dont require a computer, a subscription, or any special skills. Just a few minutes and a willingness to try something new. We cover the best brain exercises for seniors, how they work, and how to make them a fun part of your daily routine.</p>'
    ),
    (
        '<p>Your brain is made up of billions of nerve cells called neurons. Throughout your life, these neurons form connections with each other. Every time you learn something new, you build new pathways. This ability is called <strong>neuroplasticity</strong>, and it continues well into your 80s and 90s.</p>',
        '<p>Your brain is made up of billions of nerve cells called neurons. Throughout your life, these neurons form connections. Every time you learn something new, you build new pathways. This ability is called <strong>neuroplasticity</strong>, and it continues well into your 80s and 90s.</p>'
    ),
    (
        '<div class="tip-box">\n<strong>Did you know?</strong> A landmark study published in JAMA Neurology found that seniors who engaged in mentally stimulating activities like reading, puzzles, and learning new skills had a 47% lower rate of mild cognitive impairment over five years compared to those who did not.\n</div>',
        '<div class="tip-box">\n<strong>Did you know?</strong> A landmark study in JAMA Neurology found that seniors who did mentally stimulating activities like reading, puzzles, and learning new skills had a 47% lower rate of mild cognitive impairment over five years compared to those who didnt.\n</div>'
    ),
    (
        '<p>Here are seven easy activities you can start today. Most take just 10\u201315 minutes and require no special equipment.</p>',
        '<p>Here are seven easy activities you can start today. Most take just 10-15 minutes and require no special equipment.</p>'
    ),
    (
        '<p>Consistency matters more than intensity. Here\'s a simple daily plan:</p>',
        '<p>Consistency matters more than intensity. Heres a simple daily plan:</p>'
    ),
    (
        '<p>Mix up your activities throughout the week. Variety is important \u2014 doing the same puzzle every day only exercises one part of your brain. Try to rotate through different types of mental challenges.</p>',
        '<p>Mix up your activities throughout the week. Variety is important. Doing the same puzzle every day only exercises one part of your brain. Try rotating through different types of mental challenges.</p>'
    ),
    (
        '<p>Physical exercise and mental stimulation work together. When you move your body, you increase blood flow to your brain, which supports memory and thinking. For the best results, combine brain games with regular physical activity.</p>',
        '<p>Physical exercise and mental stimulation work together. When you move your body, you increase blood flow to your brain. That supports memory and thinking. For the best results, combine brain games with regular physical activity.</p>'
    ),
    (
        '<p>A: Even 10\u201315 minutes a day makes a difference. Research shows that consistency \u2014 doing a little every day \u2014 is far more effective than doing a lot once a week.</p>',
        '<p>A: Even 10-15 minutes a day makes a difference. Research shows that consistency, doing a little every day, is far more effective than doing a lot once a week.</p>'
    ),
    (
        '<p>A: Some are helpful, but they\'re not necessary. Free activities like crosswords, reading, and puzzles are just as effective, if not more so. The most important factor is that you enjoy the activity and do it regularly.</p>',
        '<p>A: Some are helpful, but theyre not necessary. Free activities like crosswords, reading, and puzzles are just as effective, if not more so. The most important thing is that you enjoy the activity and do it regularly.</p>'
    ),
    (
        '<p>A: Absolutely not. Neuroplasticity \u2014 your brain\'s ability to form new connections \u2014 continues throughout life. People in their 80s and 90s who start new mental activities show measurable improvements in memory and processing speed. It\'s never too late to start.</p>',
        '<p>A: Absolutely not. Neuroplasticity, your brains ability to form new connections, continues throughout life. People in their 80s and 90s who start new mental activities show real improvements in memory and processing speed. Its never too late to start.</p>'
    ),
    (
        '<p>Pick one activity from this list and try it tomorrow morning. Notice how it feels to challenge your brain. Then try another one the next day. Before long, you\'ll have a daily mental fitness routine that keeps you sharp, engaged, and curious about the world.</p>',
        '<p>Pick one activity from this list and try it tomorrow morning. Notice how it feels to challenge your brain. Then try another one the next day. Before long, youll have a daily mental fitness routine that keeps you sharp, engaged, and curious about the world.</p>'
    ),
]

f = os.path.join(BASE, "brain-games-seniors.html")
result = humanize_article(f, brain_replacements)
print(f"  Result: {'OK' if result else 'FAILED'}")

# ============================================================
# ARTICLE 6: stretching-routines-seniors.html
# ============================================================
print("=== Article 6: stretching-routines-seniors.html ===")

stretch_replacements = [
    (
        '<p>Do you wake up feeling stiff and creaky? Do everyday movements like reaching for a cup, bending to tie your shoes, or turning to look behind you feel harder than they used to? You are not alone. Age-related stiffness and loss of flexibility affect most seniors, but here is the good news: <strong>gentle, consistent stretching can reverse much of this decline.</strong></p>',
        '<p>Do you wake up feeling stiff and creaky? Do everyday movements like reaching for a cup, bending to tie your shoes, or turning to look behind you feel harder than they used to? Youre not alone. Age-related stiffness affects most seniors. But heres the good news: <strong>gentle, consistent stretching can reverse much of this decline.</strong></p>'
    ),
    (
        '<p>Stretching is one of the safest and most effective ways for seniors to maintain independence, prevent injury, and feel better in their bodies every day. Unlike high-impact exercise, stretches are gentle on joints, require no equipment, and can be done from the comfort of your home \u2014 seated or standing.</p>',
        '<p>Stretching is one of the safest and most effective ways for seniors to maintain independence, prevent injury, and feel better every day. Unlike high-impact exercise, stretches are gentle on joints, require no equipment, and can be done from the comfort of your home, seated or standing.</p>'
    ),
    (
        '<p>This guide covers everything you need to know about stretching for seniors: why flexibility matters, a complete daily stretching routine, safety tips, and how to make stretching a lasting habit.</p>',
        '<p>This guide covers why flexibility matters, a complete daily stretching routine, safety tips, and how to make stretching a lasting habit.</p>'
    ),
    (
        '<div class="tip-box">\n<strong>Safety First:</strong> Always consult your doctor before starting any new exercise or stretching program, especially if you have joint replacements, osteoporosis, or chronic conditions. Stretch gently \u2014 you should feel a mild pull, never sharp pain. Stop immediately if you feel discomfort.\n</div>',
        '<div class="tip-box">\n<strong>Safety First:</strong> Always check with your doctor before starting any new exercise or stretching program, especially if you have joint replacements, osteoporosis, or chronic conditions. Stretch gently. You should feel a mild pull, never sharp pain. Stop immediately if you feel discomfort.\n</div>'
    ),
    (
        '<p>As we age, our muscles, tendons, and connective tissues naturally lose elasticity. This process, called fibrosis, causes muscles to become stiffer and shorter. Joints produce less synovial fluid, the natural lubricant that keeps movement smooth. The result: reduced range of motion, morning stiffness, and a higher risk of muscle strains and falls.</p>',
        '<p>As we age, our muscles, tendons, and connective tissues naturally lose elasticity. This process, called fibrosis, makes muscles stiffer and shorter. Joints produce less synovial fluid, the natural lubricant that keeps movement smooth. The result is reduced range of motion, morning stiffness, and a higher risk of strains and falls.</p>'
    ),
    (
        '<p><strong>But here is the encouraging truth:</strong> research shows that regular stretching can significantly improve flexibility at any age. A 2023 study of adults over 65 found that those who stretched for just 15 minutes daily, five days per week, improved their hip and shoulder range of motion by an average of 25% over eight weeks.</p>',
        '<p><strong>But heres the encouraging truth:</strong> research shows that regular stretching can significantly improve flexibility at any age. A 2023 study of adults over 65 found that those who stretched for just 15 minutes daily, five days per week, improved their hip and shoulder range of motion by an average of 25% over eight weeks.</p>'
    ),
    (
        '<div class="tip-box">\n<strong>Did You Know?</strong> Flexibility is one of the five components of health-related fitness, alongside cardiovascular endurance, muscular strength, muscular endurance, and body composition. Yet it is often the most neglected. Prioritizing flexibility can transform how you feel every single day.\n</div>',
        '<div class="tip-box">\n<strong>Did You Know?</strong> Flexibility is one of the five components of health-related fitness, alongside cardiovascular endurance, muscular strength, muscular endurance, and body composition. Yet its often the most neglected. Prioritizing flexibility can transform how you feel every single day.\n</div>'
    ),
    (
        '<p>This routine is designed for seniors of all fitness levels. It takes just 10 minutes and requires no equipment. Each stretch can be done seated or standing, depending on your balance and comfort. Begin each stretch gently and never force a position.</p>',
        '<p>This routine is designed for seniors of all fitness levels. It takes just 10 minutes and requires no equipment. Each stretch can be done seated or standing, depending on your balance and comfort. Start gently and never force a position.</p>'
    ),
    (
        '<p>Even gentle stretching benefits from a proper warm-up and cool-down. Warming up prepares your muscles and joints for movement, reducing the risk of strain. Cooling down helps your body return to a resting state and reinforces the benefits of your stretching session.</p>',
        '<p>Even gentle stretching benefits from a proper warm-up and cool-down. Warming up prepares your muscles and joints for movement and reduces the risk of strain. Cooling down helps your body return to a resting state and reinforces the benefits of your stretching session.</p>'
    ),
    (
        '<div class="tip-box">\n<strong>Pro Tip:</strong> The best time to stretch is after a warm shower or bath, when your muscles are already warm and pliable. Evening stretching before bed can also improve sleep quality by releasing the day\'s physical tension.\n</div>',
        '<div class="tip-box">\n<strong>Pro Tip:</strong> The best time to stretch is after a warm shower or bath, when your muscles are already warm and pliable. Evening stretching before bed can also improve sleep quality by releasing the days physical tension.\n</div>'
    ),
    (
        '<p>Stretching is safe for seniors, but a few precautions will help you get you the best results with the lowest risk. Follow these guidelines every time.</p>',
        '<p>Stretching is safe for seniors, but a few precautions will help you get the best results with the lowest risk. Follow these guidelines every time.</p>'
    ),
    (
        '<p>Knowing the stretches is only half the battle. The real magic happens when stretching becomes a regular part of your day. Here is how to build a stretching habit that sticks.</p>',
        '<p>Knowing the stretches is only half the battle. The real magic happens when stretching becomes a regular part of your day. Heres how to build a habit that sticks.</p>'
    ),
    (
        '<p>A: Morning stretching helps wake up stiff muscles and joints after a night\'s rest. Evening stretching can promote relaxation and better sleep. Choose a time when your muscles are warm \u2014 after a warm shower or a short walk is ideal.</p>',
        '<p>A: Morning stretching helps wake up stiff muscles and joints after a nights rest. Evening stretching can promote relaxation and better sleep. Pick a time when your muscles are warm. After a warm shower or a short walk is ideal.</p>'
    ),
    (
        '<p>A: Yes. While flexibility naturally declines with age, regular stretching can significantly improve range of motion at any age. Studies show seniors who stretch consistently for 4-6 weeks see measurable improvements in flexibility and reduced stiffness.</p>',
        '<p>A: Yes. While flexibility naturally declines with age, regular stretching can significantly improve your range of motion at any age. Studies show seniors who stretch consistently for 4-6 weeks see real improvements in flexibility and less stiffness.</p>'
    ),
    (
        '<p>A: Dynamic stretching (gentle movement-based stretches) is best before exercise. Save static holding stretches for after exercise when muscles are warm. A 5-minute warm-up of marching in place followed by gentle movement stretches prepares the body safely.</p>',
        '<p>A: Dynamic stretching, gentle movement-based stretches, is best before exercise. Save static holding stretches for after exercise when muscles are warm. A 5-minute warm-up of marching in place followed by gentle movement stretches prepares the body safely.</p>'
    ),
    (
        '<h2>Start Stretching Today \u2014 Your Body Will Thank You</h2>',
        '<h2>Start Stretching Today and Your Body Will Thank You</h2>'
    ),
    (
        '<p>Flexibility is not about touching your toes or doing splits. It is about moving through your day with ease, comfort, and confidence. It is about reaching for a dish on a high shelf without wincing. It is about getting out of a chair without using your hands. It is about playing with your grandchildren without worrying about pulling a muscle.</p>',
        '<p>Flexibility isnt about touching your toes or doing splits. Its about moving through your day with ease, comfort, and confidence. Its about reaching for a dish on a high shelf without wincing. Getting out of a chair without using your hands. Playing with your grandchildren without worrying about pulling a muscle.</p>'
    ),
    (
        '<p>The seven stretches in this routine take just 10 minutes \u2014 less time than it takes to watch a TV commercial break. In exchange for those 10 minutes, you gain greater independence, reduced pain, and a body that feels younger than your calendar says.</p>',
        '<p>The seven stretches in this routine take just 10 minutes. Less time than it takes to watch a TV commercial break. In exchange for those 10 minutes, you gain greater independence, less pain, and a body that feels younger than your calendar says.</p>'
    ),
    (
        '<p><strong>Here is your first step:</strong> Right now, wherever you are, take three slow, deep breaths. Roll your shoulders back three times. Gently tilt your head side to side. Congratulations \u2014 you have started your stretching journey. Tomorrow, try the full routine. Keep going, and within two weeks, you will feel a difference you can notice.</p>',
        '<p><strong>Here is your first step:</strong> Right now, wherever you are, take three slow, deep breaths. Roll your shoulders back three times. Gently tilt your head side to side. Congratulations, you have started your stretching journey. Tomorrow, try the full routine. Keep going, and within two weeks, you will feel a difference you can notice.</p>'
    ),
]

f = os.path.join(BASE, "stretching-routines-seniors.html")
result = humanize_article(f, stretch_replacements)
print(f"  Result: {'OK' if result else 'FAILED'}")

# ============================================================
# ARTICLE 7: low-impact-cardio-seniors.html
# ============================================================
print("=== Article 7: low-impact-cardio-seniors.html ===")

cardio_replacements = [
    (
        '<p>Staying active after 65 doesn\'t mean you need to run marathons or lift heavy weights. In fact, some of the best exercise for your heart is <strong>gentle, steady, and low-impact</strong>. Low-impact cardio raises your heart rate without stressing your joints \u2014 making it ideal for seniors who want to stay fit, mobile, and independent.</p>',
        '<p>Staying active after 65 doesnt mean you need to run marathons or lift heavy weights. In fact, some of the best exercise for your heart is <strong>gentle, steady, and low-impact</strong>. Low-impact cardio raises your heart rate without stressing your joints. That makes it ideal for seniors who want to stay fit, mobile, and independent.</p>'
    ),
    (
        '<p>This guide covers everything you need to know about low-impact cardio for seniors. You will learn why it matters, how to get started safely, and five simple routines you can do from the comfort of your living room.</p>',
        '<p>We cover everything you need to know about low-impact cardio for seniors. Youll learn why it matters, how to start safely, and five simple routines you can do from your living room.</p>'
    ),
    (
        '<div class="tip-box">\n<strong>Safety First:</strong> Always consult your doctor before starting any new exercise program, especially if you have heart conditions, joint issues, or have been inactive for a while. Listen to your body. If something hurts, stop.\n</div>',
        '<div class="tip-box">\n<strong>Safety First:</strong> Always check with your doctor before starting any new exercise program, especially if you have heart conditions, joint issues, or have been inactive for a while. Listen to your body. If something hurts, stop.\n</div>'
    ),
    (
        '<p>Your heart is a muscle, and like any muscle, it needs regular exercise to stay strong. As we age, our cardiovascular system naturally changes. Blood vessels become stiffer, heart rate may slow, and endurance can decline. But here is the good news: regular low-impact cardio can slow these changes and even reverse some of them.</p>',
        '<p>Your heart is a muscle. Like any muscle, it needs regular exercise to stay strong. As we age, our cardiovascular system naturally changes. Blood vessels become stiffer. Heart rate may slow. Endurance can decline. But heres the good news: regular low-impact cardio can slow these changes and even reverse some of them.</p>'
    ),
    (
        '<p>The beauty of low-impact cardio is that it is <strong>gentle enough for beginners</strong> yet effective enough to deliver real health benefits. You do not need special equipment, a gym membership, or prior exercise experience.</p>',
        '<p>The beauty of low-impact cardio is that its <strong>gentle enough for beginners</strong> yet effective enough to deliver real health benefits. You dont need special equipment, a gym membership, or prior exercise experience.</p>'
    ),
    (
        '<p>Before you begin any cardio routine, take a few minutes to prepare. A small investment in safety pays big dividends in long-term success.</p>',
        '<p>Before you begin any cardio routine, take a few minutes to prepare. A small investment in safety pays off in the long run.</p>'
    ),
    (
        '<p>During exercise, you should feel your heart beating faster and your breathing deepen, but you should never feel sharp pain, dizziness, or chest tightness. If you experience any of these, stop immediately and rest.</p>',
        '<p>During exercise, you should feel your heart beating faster and your breathing deepen. But you should never feel sharp pain, dizziness, or chest tightness. If you experience any of these, stop immediately and rest.</p>'
    ),
    (
        '<p>Do not aim for perfection. Aim for consistency. Ten minutes of gentle movement every day is far better than an hour once a week. Build up slowly and celebrate every small victory.</p>',
        '<p>Dont aim for perfection. Aim for consistency. Ten minutes of gentle movement every day is far better than an hour once a week. Build up slowly and celebrate every small victory.</p>'
    ),
    (
        '<p>Here are five simple cardio exercises you can do at home. No equipment needed. Each exercise can be done seated or standing, depending on your balance and comfort level.</p>',
        '<p>Here are five simple cardio exercises you can do at home. No equipment needed. Each one can be done seated or standing, depending on your balance and comfort level.</p>'
    ),
    (
        '<p>Now that you know the exercises, let\'s put them together into a simple weekly plan. Remember: consistency matters more than intensity.</p>',
        '<p>Now that you know the exercises, lets put them together into a simple weekly plan. Remember, consistency matters more than intensity.</p>'
    ),
    (
        '<div class="tip-box">\n<strong>Pro Tip:</strong> Use the \"talk test\" to gauge your intensity. You should be breathing harder than normal but still able to speak in full sentences. If you cannot talk comfortably, slow down.\n</div>',
        '<div class="tip-box">\n<strong>Pro Tip:</strong> Use the \"talk test\" to gauge your intensity. You should be breathing harder than normal but still able to speak in full sentences. If you cant talk comfortably, slow down.\n</div>'
    ),
    (
        '<p>A: The CDC recommends seniors get at least 150 minutes of moderate-intensity aerobic activity per week. That breaks down to about 30 minutes, 5 days a week. Start with 10-15 minute sessions if you are new to exercise.</p>',
        '<p>A: The CDC recommends seniors get at least 150 minutes of moderate-intensity aerobic activity per week. That breaks down to about 30 minutes, 5 days a week. Start with 10-15 minute sessions if youre new to exercise.</p>'
    ),
    (
        '<p>A: A simpler approach than counting beats is the \"talk test\": you should be breathing harder but still able to carry on a conversation. Always consult your doctor for personalized guidance.</p>',
        '<p>A: A simpler approach than counting beats is the \"talk test.\" You should be breathing harder but still able to carry on a conversation. Always check with your doctor for personalized guidance.</p>'
    ),
    (
        '<p>Low-impact cardio is one of the kindest things you can do for your body after 65. It strengthens your heart, lifts your spirits, and keeps you independent longer. You do not need fancy equipment or a gym. You just need a comfortable chair, a water bottle, and the willingness to start.</p>',
        '<p>Low-impact cardio is one of the kindest things you can do for your body after 65. It strengthens your heart, lifts your spirits, and keeps you independent longer. You dont need fancy equipment or a gym. Just a comfortable chair, a water bottle, and the willingness to start.</p>'
    ),
    (
        '<p>Pick one exercise from this guide \u2014 marching in place is a great choice \u2014 and try it for five minutes today. Tomorrow, try five minutes again. Before you know it, those five minutes will become ten, then twenty, then a lasting habit that keeps you strong and healthy for years to come.</p>',
        '<p>Pick one exercise from this guide. Marching in place is a great choice. Try it for five minutes today. Tomorrow, try five minutes again. Before you know it, those five minutes will become ten, then twenty, then a lasting habit that keeps you strong and healthy for years to come.</p>'
    ),
]

f = os.path.join(BASE, "low-impact-cardio-seniors.html")
result = humanize_article(f, cardio_replacements)
print(f"  Result: {'OK' if result else 'FAILED'}")

# ============================================================
# ARTICLE 8: sleep-tips-seniors.html
# ============================================================
print("=== Article 8: sleep-tips-seniors.html ===")

sleep_replacements = [
    (
        '<p>Getting a good night\'s rest is one of the most powerful things you can do for your health at any age. But for seniors 65 and older, quality sleep can feel harder to come by. You\'re not alone \u2014 research from the <a href="https://www.nia.nih.gov/health/sleep" target="_blank" rel="noopener">National Institute on Aging</a> shows that sleep changes are a normal part of aging, but poor sleep doesn\'t have to be your new normal.</p>',
        '<p>Getting a good nights rest is one of the most powerful things you can do for your health at any age. But for seniors 65 and older, quality sleep can feel harder to come by. Youre not alone. Research from the <a href="https://www.nia.nih.gov/health/sleep" target="_blank" rel="noopener">National Institute on Aging</a> shows that sleep changes are a normal part of aging. But poor sleep doesnt have to be your new normal.</p>'
    ),
    (
        '<p>This guide covers <strong>natural sleep tips for seniors</strong> that are safe, effective, and backed by science. Whether you\'re dealing with trouble falling asleep, waking up too early, or feeling tired all day, these strategies can help.</p>',
        '<p>This guide covers <strong>natural sleep tips for seniors</strong> that are safe, effective, and backed by science. Whether youre dealing with trouble falling asleep, waking up too early, or feeling tired all day, these strategies can help.</p>'
    ),
    (
        '<p>As we get older, our bodies produce less melatonin \u2014 the natural hormone that signals it\'s time to sleep. Our internal body clock also shifts, making us feel tired earlier and wake up earlier. These changes are normal, but they don\'t mean you have to accept poor sleep.</p>',
        '<p>As we get older, our bodies produce less melatonin, the natural hormone that signals its time to sleep. Our internal body clock also shifts, making us feel tired earlier and wake up earlier. These changes are normal. But they dont mean you have to accept poor sleep.</p>'
    ),
    (
        '<p>Many of these issues can be improved with simple lifestyle adjustments. The right sleep habits, or \"sleep hygiene,\" make a noticeable difference \u2014 often within a few days.</p>',
        '<p>Many of these issues can be improved with simple lifestyle adjustments. The right sleep habits make a noticeable difference, often within a few days.</p>'
    ),
    (
        '<p>A calm, predictable evening routine tells your body it\'s time to wind down. Here\'s what works for most seniors:</p>',
        '<p>A calm, predictable evening routine tells your body its time to wind down. Heres what works for most seniors:</p>'
    ),
    (
        '<p>Go to bed and wake up at the same time every day \u2014 even on weekends. This trains your body\'s internal clock and makes falling asleep easier over time.</p>',
        '<p>Go to bed and wake up at the same time every day, even on weekends. This trains your bodys internal clock and makes falling asleep easier over time.</p>'
    ),
    (
        '<p>What you do during the day has a huge impact on how well you sleep at night. These changes don\'t require special equipment or expensive products:</p>',
        '<p>What you do during the day has a huge impact on how well you sleep at night. These changes dont require special equipment or expensive products:</p>'
    ),
    (
        '<p>Exposure to natural light early in the day helps reset your internal clock. Spend 15\u201320 minutes outside in the morning \u2014 even on cloudy days. This simple habit is one of the most effective <strong>sleep tips for seniors</strong> we know.</p>',
        '<p>Exposure to natural light early in the day helps reset your internal clock. Spend 15-20 minutes outside in the morning, even on cloudy days. This simple habit is one of the most effective <strong>sleep tips for seniors</strong> we know.</p>'
    ),
    (
        '<p>A short \"power nap\" of 20 minutes can be refreshing. Longer naps, especially after 3 p.m., can make it harder to fall asleep at night. If you\'re tired during the day, try a short walk or standing up and moving instead of lying down.</p>',
        '<p>A short power nap of 20 minutes can be refreshing. Longer naps, especially after 3 p.m., can make it harder to fall asleep at night. If youre tired during the day, try a short walk or standing up and moving instead of lying down.</p>'
    ),
    (
        '<p>A: Melatonin can help some people, but it\'s important to talk to your doctor first, especially if you take blood thinners or other medications. Start with a low dose (0.5\u20131 mg) and use it short-term.</p>',
        '<p>A: Melatonin can help some people, but its important to talk to your doctor first, especially if you take blood thinners or other medications. Start with a low dose (0.5-1 mg) and use it short-term.</p>'
    ),
    (
        '<p>Quality sleep is not a luxury \u2014 it\'s essential for your health, memory, mood, and energy. By making small, consistent changes to your daily routine, you can improve how well you sleep and how good you feel.</p>',
        '<p>Quality sleep is not a luxury. Its essential for your health, memory, mood, and energy. By making small, consistent changes to your daily routine, you can improve how well you sleep and how good you feel.</p>'
    ),
]

f = os.path.join(BASE, "sleep-tips-seniors.html")
result = humanize_article(f, sleep_replacements)
print(f"  Result: {'OK' if result else 'FAILED'}")

print("\n=== DONE ===")