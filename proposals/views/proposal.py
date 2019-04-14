import logging

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import View

from conference.models.event import Event
from pyconlt.settings.base import CURRENT_EVENT
from ..forms import ReviewForm
from ..models.proposal import Proposal
from ..models.review import Review

logger = logging.getLogger(__name__)


class ProposalReviewView(View):
    """Displaying all reviews for single Proposal for presenters."""
    template = "proposals/proposal_detail.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if not request.user.has_perm("auth.is_committee_member"):
            return HttpResponseForbidden()

        proposal_id = self.kwargs.get("pk")

        proposal = get_object_or_404(Proposal, pk=proposal_id)
        reviews = Review.objects.filter(proposal=proposal_id)

        try:
            status = Review.objects.get(
                author=request.user,
                proposal_id=proposal_id).status
        except:
            status = 0

        context = {"proposal": proposal, "reviews": reviews, "status": status}

        return render(request, self.template, context)


class ProposalsView(View):
    """Displaying proposals that are ready to be reviewed."""
    template = "proposals/proposals_to_review.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if not request.user.has_perm("auth.is_committee_member"):
            return HttpResponseForbidden()

        event = Event.objects.filter(year=CURRENT_EVENT).first()

        if event:
            proposals = Proposal.objects.filter(event=event.pk, state=0)

        context = {"proposals": proposals if event else None}

        return render(request, self.template, context)
