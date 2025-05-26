"""
Configuration parameters for Post This Today
"""

# Site Information
SITE_NAME = "Post This Today"
SITE_TAGLINE = "AI-Powered LinkedIn Content Creation"
SITE_DESCRIPTION = "Create engaging LinkedIn posts in minutes with AI that matches your writing style"

# Feature Descriptions
FEATURES = [
    {
        'title': 'AI Writing Style Analysis',
        'description': 'Upload your writing samples and our AI learns your unique voice and tone',
        'icon': 'brain'
    },
    {
        'title': 'Trending Topics Integration',
        'description': 'Stay relevant with real-time trending topics from your industry',
        'icon': 'trending-up'
    },
    {
        'title': 'Multiple Tone Options',
        'description': 'Switch between professional, funny, sensitive, or hard-hitting tones',
        'icon': 'sliders'
    },
    {
        'title': 'LinkedIn-Optimized Format',
        'description': 'Content formatted perfectly for maximum LinkedIn engagement',
        'icon': 'linkedin'
    },
    {
        'title': 'One-Click Sharing',
        'description': 'Share directly to LinkedIn or copy to clipboard instantly',
        'icon': 'share-2'
    },
    {
        'title': 'Writing Samples Library',
        'description': 'Build a library of your best writing for consistent AI training',
        'icon': 'library'
    }
]

# Workflow Steps
WORKFLOW_STEPS = [
    {
        'number': '1',
        'title': 'Upload Writing Samples',
        'description': 'Share examples of your writing style for AI analysis',
        'icon': 'upload'
    },
    {
        'number': '2',
        'title': 'Select Trending Topic',
        'description': 'Choose from current trending topics in your industry',
        'icon': 'trending-up'
    },
    {
        'number': '3',
        'title': 'Add Your Angle',
        'description': 'Provide specific points or perspectives you want to cover',
        'icon': 'edit-3'
    },
    {
        'number': '4',
        'title': 'Customize Tone & Length',
        'description': 'Fine-tune the tone, length, and additional topics',
        'icon': 'settings'
    },
    {
        'number': '5',
        'title': 'Preview & Share',
        'description': 'Review your AI-generated post and share to LinkedIn',
        'icon': 'send'
    }
]

# FAQ Content
FAQ_ITEMS = [
    {
        'question': 'How does the AI analyze my writing style?',
        'answer': 'Our AI uses advanced natural language processing to analyze patterns in your writing samples, including vocabulary, sentence structure, tone, and formatting preferences. This creates a unique writing profile that ensures generated content matches your voice.'
    },
    {
        'question': 'Is my data secure?',
        'answer': 'Absolutely. We use industry-standard encryption for all data transmission and storage. Your writing samples and generated content are never shared with third parties, and you can delete your data at any time.'
    },
    {
        'question': 'How much does it cost?',
        'answer': 'Post This Today is currently free to use during our beta period. We\'re gathering feedback to improve the service before introducing premium plans.'
    },
    {
        'question': 'Can I edit the generated content?',
        'answer': 'Yes! The AI-generated content is a starting point. You can edit, refine, or completely rewrite any part before sharing. Many users find they only need minor tweaks to match their exact voice.'
    },
    {
        'question': 'What makes this different from other AI writers?',
        'answer': 'Post This Today is specifically designed for LinkedIn content creation. We combine your unique writing style with trending topics and LinkedIn best practices to create posts that get engagement.'
    },
    {
        'question': 'How often are trending topics updated?',
        'answer': 'Trending topics are updated multiple times daily from various industry sources, ensuring you always have fresh, relevant content ideas to work with.'
    }
]

# Call-to-Action Text
CTA_PRIMARY = "Get Started Free"
CTA_SECONDARY = "See How It Works"
CTA_LEARN_MORE = "Learn More"

# Navigation Items
NAV_ITEMS_PUBLIC = [
    {'name': 'Home', 'url': '/'},
    {'name': 'About', 'url': '/about/'},
    {'name': 'Pricing', 'url': '/pricing/'},
]

NAV_ITEMS_AUTH = [
    {'name': 'Create Post', 'url': '/app/'},
    {'name': 'History', 'url': '/history/'},
    {'name': 'Settings', 'url': '/settings/'},
]

# Color Scheme (for reference in templates)
COLORS = {
    'primary': 'purple-800',  # #7c2d92
    'primary_hover': 'purple-900',
    'secondary': 'stone-200',
    'background': 'stone-50',
    'text_primary': 'gray-900',
    'text_secondary': 'gray-600',
}

# Pricing Tiers (for future use)
PRICING_TIERS = [
    {
        'name': 'Free',
        'price': '$0',
        'period': 'forever',
        'features': [
            '10 posts per month',
            'Basic AI analysis',
            'Standard templates',
            'LinkedIn sharing'
        ],
        'cta': 'Start Free',
        'highlighted': False
    },
    {
        'name': 'Pro',
        'price': '$19',
        'period': 'per month',
        'features': [
            'Unlimited posts',
            'Advanced AI analysis',
            'Custom templates',
            'Priority support',
            'Analytics dashboard',
            'Team collaboration'
        ],
        'cta': 'Go Pro',
        'highlighted': True
    },
    {
        'name': 'Enterprise',
        'price': 'Custom',
        'period': 'contact us',
        'features': [
            'Everything in Pro',
            'Custom AI training',
            'API access',
            'Dedicated support',
            'Custom integrations',
            'SLA guarantee'
        ],
        'cta': 'Contact Sales',
        'highlighted': False
    }
]