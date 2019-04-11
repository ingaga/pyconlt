from django.conf.urls import url

from proposals.views.cfp import CFPView
from proposals.views.manage import ProposalDeleteView, ProposalListView, ProposalUpdateView
from proposals.views.proposal import ProposalView, ProposalsViews
from proposals.views.review import ReviewView

urlpatterns = [
    url(r'(?P<pk>\d+)/proposal', ProposalView.as_view()),
    url(r'review_list/$', ProposalsViews.as_view(), name="review_list"),
    url(r'(?P<pk>\d+)/cfp_form', CFPView.as_view()),
    url(r'^$', ProposalListView.as_view(), name='proposal_list'),
    url(r'(?P<pk>\d+)/delete',
        ProposalDeleteView.as_view(),
        name='proposal_delete'
    ),
    url(r'(?P<pk>\d+)/update',
        ProposalUpdateView.as_view(),
        name='proposal_update'
    ),
    url(r'(?P<pk>\d+)/review',
        ReviewView.as_view(),
        name='review_view'
    )
]
