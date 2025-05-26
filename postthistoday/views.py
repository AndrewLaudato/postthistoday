"""
Post This Today - Django Views
Content creation workflow views for LinkedIn post generation
"""

from django.shortcuts import render, redirect

# =============================================================================
# CONSTANTS & DATA
# =============================================================================

# Mock trending topics data (will be replaced with live API data later)
TRENDING_TOPICS_DATA = [
    {
        'id': 1,
        'title': 'AI Technology Breakthrough: New Language Model Sets Performance Records',
        'category': 'Technology',
        'source': 'Tech Daily',
        'time': '2 hours ago',
    },
    {
        'id': 2,
        'title': 'Remote Work Revolution: Major Companies Announce Permanent Hybrid Models',
        'category': 'Business',
        'source': 'Business Insider',
        'time': '4 hours ago',
    },
    {
        'id': 3,
        'title': 'Sustainable Innovation: Breakthrough in Renewable Energy Storage',
        'category': 'Science',
        'source': 'Science Weekly',
        'time': '6 hours ago',
    },
    {
        'id': 4,
        'title': 'Digital Transformation: Small Businesses Embrace E-commerce Solutions',
        'category': 'Business',
        'source': 'Industry News',
        'time': '8 hours ago',
    },
]

# Workflow configuration
TOTAL_STEPS = 5

##not logged in pages

# Add these imports at the top of your views.py file:
from django.shortcuts import render, redirect
from . import parms  # Import the configuration parameters


# Add these view functions to your existing views.py:

def landing_page(request):
    """
    Public landing page for Post This Today
    """
    if request.user.is_authenticated:
        return redirect('app_home')

    context = {
        'site_name': parms.SITE_NAME,
        'site_tagline': parms.SITE_TAGLINE,
        'site_description': parms.SITE_DESCRIPTION,
        'features': parms.FEATURES,
        'workflow_steps': parms.WORKFLOW_STEPS,
        'faq_items': parms.FAQ_ITEMS,
        'cta_primary': parms.CTA_PRIMARY,
        'cta_secondary': parms.CTA_SECONDARY,
    }
    return render(request, 'landing_page.html', context)


def about_page(request):
    """
    About page for Post This Today
    """
    context = {
        'site_name': parms.SITE_NAME,
        'site_tagline': parms.SITE_TAGLINE,
        'site_description': parms.SITE_DESCRIPTION,
        'features': parms.FEATURES,
    }
    return render(request, 'about.html', context)


def pricing_page(request):
    """
    Pricing page for Post This Today
    """
    context = {
        'site_name': parms.SITE_NAME,
        'pricing_tiers': parms.PRICING_TIERS,
    }
    return render(request, 'pricing.html', context)


def mystyle(request):
    """
    Updated function name for the first step of the workflow
    This replaces the old writing_samples function
    """
    if request.method == 'POST':
        # TODO: Handle file upload processing
        # Navigate to step 2
        return redirect('trending_topics')

    context = {
        'current_step': 1,
        'total_steps': TOTAL_STEPS,
        'step_name': 'My Style'
    }
    return render(request, 'postthistoday/mystyle.html', context)







# =============================================================================
# STEP VIEWS - 5-Step Content Creation Workflow
# =============================================================================

def mystyle(request):
    if request.method == 'POST':
        # TODO: Handle file upload processing
        # Navigate to step 2
        return redirect('trending_topics')

    context = {
        'current_step': 1,
        'total_steps': TOTAL_STEPS,
        'step_name': 'Writing Samples'
    }
    return render(request, 'postthistoday/mystyle.html', context)


def trending_topics(request):
    """
    Step 2: Trending Topics Selection

    Displays current trending topics from various sources and allows
    users to select one as the basis for their content.

    GET: Display trending topics list
    POST: Save selected topic and navigate to step 3
    """
    if request.method == 'POST':
        selected_topic = request.POST.get('selected_topic')

        # Store selected topic in session for use in later steps
        request.session['selected_topic'] = selected_topic

        # Navigate to step 3
        return redirect('content_prompt')

    context = {
        'current_step': 2,
        'total_steps': TOTAL_STEPS,
        'step_name': 'Trending Topics',
        'trending_topics': TRENDING_TOPICS_DATA,
        'selected_topic': request.session.get('selected_topic', '')
    }
    return render(request, 'postthistoday/trending_topics.html', context)


def content_prompt(request):
    """
    Step 3: Content Prompt Creation

    Allow users to add specific details, angles, or key points
    they want to include in their content.

    GET: Display prompt input interface
    POST: Save content prompt and navigate to step 4
    """
    if request.method == 'POST':
        content_prompt_text = request.POST.get('content_prompt', '').strip()

        # Store content prompt in session
        request.session['content_prompt'] = content_prompt_text

        # Navigate to step 4
        return redirect('customize_content')

    context = {
        'current_step': 3,
        'total_steps': TOTAL_STEPS,
        'step_name': 'Content Prompt',
        'selected_topic': request.session.get('selected_topic', ''),
        'content_prompt': request.session.get('content_prompt', '')
    }
    return render(request, 'postthistoday/content_prompt.html', context)


# Temporarily add these print statements to your customize_content function in views.py:

def customize_content(request):
    """
    Step 4: Content Customization
    """
    print("🔵 customize_content view called")  # Add this

    if request.method == 'POST':
        print("🔵 POST request received in customize_content")  # Add this

        tone = request.POST.get('tone')
        length = request.POST.get('length')
        topics = request.POST.getlist('topics')

        print(f"🔵 Form data: tone={tone}, length={length}, topics={topics}")  # Add this

        # Store customization preferences in session
        request.session['tone'] = tone
        request.session['length'] = length
        request.session['custom_topics'] = topics

        print("🔵 About to import call_ai...")  # Add this

        # Generate AI content using all collected data
        from . import call_ai

        print("🔵 call_ai imported successfully")  # Add this
        print("🔵 About to call generate_linkedin_post...")  # Add this

        ai_result = call_ai.generate_linkedin_post(
            selected_topic=request.session.get('selected_topic', ''),
            content_prompt=request.session.get('content_prompt', ''),
            tone=tone,
            length=length,
            custom_topics=topics,
            mystyle=None
        )

        print(f"🔵 AI result received: success={ai_result.get('success')}")  # Add this
        print(f"🔵 Content preview: {ai_result.get('content', '')[:100]}...")  # Add this

        # Store AI result in session
        request.session['generated_content'] = ai_result['content']
        request.session['ai_success'] = ai_result['success']
        request.session['ai_error'] = ai_result['error']

        print("🔵 Redirecting to preview_and_share...")  # Add this

        # Navigate to step 5
        return redirect('preview_and_share')


    # Define available options
    tone_options = [
        'Professional',
        'Funny',
        'Sensitive',
        'Hard-hitting'
    ]

    length_options = [
        'Short (100-150 words)',
        'Medium (150-250 words)',
        'Long (250+ words)'
    ]

    context = {
        'current_step': 4,
        'total_steps': TOTAL_STEPS,
        'step_name': 'Customize',
        'tone_options': tone_options,
        'length_options': length_options,
        'selected_tone': request.session.get('tone', 'Professional'),
        'selected_length': request.session.get('length', 'Medium (150-250 words)'),
        'custom_topics': request.session.get('custom_topics', []),
        'selected_topic': request.session.get('selected_topic', ''),
        'content_prompt': request.session.get('content_prompt', '')
    }
    return render(request, 'postthistoday/customize_content.html', context)


def preview_and_share(request):
    """
    Step 5: Preview & Share

    Display the AI-generated content, allow editing, and provide
    options to share directly to LinkedIn or copy to clipboard.

    GET: Display generated content and sharing options
    POST: Handle content regeneration or sharing actions
    """
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'regenerate':
            # Regenerate content with AI
            from . import call_ai

            ai_result = call_ai.generate_linkedin_post(
                selected_topic=request.session.get('selected_topic', ''),
                content_prompt=request.session.get('content_prompt', ''),
                tone=request.session.get('tone', 'Professional'),
                length=request.session.get('length', 'Medium'),
                custom_topics=request.session.get('custom_topics', []),
                mystyle=None
            )

            # Update session with new AI content
            request.session['generated_content'] = ai_result['content']
            request.session['ai_success'] = ai_result['success']
            request.session['ai_error'] = ai_result['error']

        elif action == 'share_linkedin':
            # TODO: Handle LinkedIn sharing
            pass
        elif action == 'copy_clipboard':
            # TODO: Handle clipboard copy (handled by frontend)
            pass

        # Stay on same page after action
        return redirect('preview_and_share')

    # Get AI-generated content from session
    generated_content = request.session.get('generated_content', 'No content generated yet.')
    ai_success = request.session.get('ai_success', False)
    ai_error = request.session.get('ai_error', None)

    context = {
        'current_step': 5,
        'total_steps': TOTAL_STEPS,
        'step_name': 'Preview & Share',
        'selected_topic': request.session.get('selected_topic', ''),
        'content_prompt': request.session.get('content_prompt', ''),
        'tone': request.session.get('tone', ''),
        'length': request.session.get('length', ''),
        'custom_topics': request.session.get('custom_topics', []),
        'generated_content': generated_content,
        'ai_success': ai_success,
        'ai_error': ai_error
    }
    return render(request, 'postthistoday/preview_and_share.html', context)

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def get_trending_topics():
    """
    Fetch trending topics from external APIs or web scraping.

    TODO: Replace mock data with actual API calls to:
    - News APIs (NewsAPI, Guardian, etc.)
    - Social media APIs (Twitter/X, Reddit)
    - RSS feeds from major news sources

    Returns:
        list: List of trending topic dictionaries
    """
    # For now, return mock data
    return TRENDING_TOPICS_DATA


def generate_content(mystyle, selected_topic, content_prompt, tone, length, custom_topics):
    """
    Generate LinkedIn post content using AI based on user inputs.

    TODO: Integrate with AI service (OpenAI, Claude, etc.) to:
    - Analyze writing samples for style and tone
    - Create content based on selected topic and prompt
    - Apply specified tone and length preferences
    - Incorporate custom topics

    Args:
        mystyle: Uploaded writing samples
        selected_topic: Chosen trending topic
        content_prompt: User's specific content ideas
        tone: Selected tone (Professional, Funny, etc.)
        length: Desired content length
        custom_topics: Additional topics to include

    Returns:
        str: Generated LinkedIn post content
    """
    # Placeholder for AI integration
    pass