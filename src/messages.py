"""Fixed messages for the categories that never go through the RAG pipeline.

These texts are displayed word for word, never generated. Every fact was checked
against the official documents, and each message gives its source. In a real bank,
this file would be reviewed by the compliance team before any change.
"""

EMERGENCY = {
    "fr": """**Faites bloquer votre carte immédiatement (opposition).**

Vous pouvez le faire sur l'application Mes Comptes, dans votre espace client sur mabanque.bnpparibas, auprès d'un Conseiller Banque en Ligne par téléphone, en agence pendant les heures d'ouverture (déclaration écrite), ou à tout moment auprès du centre d'appels, ouvert 7 jours sur 7 et 24 h/24 (numéro non surtaxé, coût d'un appel local depuis un poste fixe en France métropolitaine) :

- Carte Origin : +33 (0) 1 40 14 03 00
- Carte VISA Classic, Carte BNP Net, Carte VISA Plus et Carte Virtuelle : +33 (0) 1 40 14 44 00
- Carte VISA Premier : +33 (0)1 40 14 10 10
- Carte VISA Infinite : +33 (0) 1 47 92 50 60

Le blocage est pris en compte immédiatement et un numéro d'enregistrement vous est communiqué. Si votre demande n'a pas été faite par une déclaration écrite et signée, confirmez-la par écrit sans délai.

Ensuite, signalez sans tarder les opérations que vous n'avez pas faites pour les contester. Je peux vous expliquer la procédure si vous me le demandez.

*Source : Conditions de fonctionnement des cartes (Contrat carte), édition avril 2026, articles XI et XVI.*""",
    "en": """**Block your card immediately.**

You can do it in the Mes Comptes app, in your online customer area on mabanque.bnpparibas, with an online adviser by phone, in your branch during opening hours (written statement), or at any time by calling the card call center, open 24/7 (no premium rate, cost of a local call from a landline in mainland France):

- Origin card: +33 (0) 1 40 14 03 00
- VISA Classic, BNP Net, VISA Plus and Virtual card: +33 (0) 1 40 14 44 00
- VISA Premier card: +33 (0)1 40 14 10 10
- VISA Infinite card: +33 (0) 1 47 92 50 60

The block takes effect immediately and you will receive a registration number. If your request was not made with a signed written statement, confirm it in writing without delay.

Then, report the transactions you did not make as soon as possible to dispute them. Ask me if you want the details of the procedure.

*Source: Conditions de fonctionnement des cartes (card contract), April 2026 edition, articles XI and XVI.*""",
}

COMPLAINT = {
    "fr": """Je suis désolé que vous ayez rencontré ce problème. Voici comment faire une réclamation.

1. **Auprès de votre agence** : contactez votre conseiller ou le directeur de votre agence, lors d'un entretien, par téléphone sur sa ligne directe, par courrier, ou via le formulaire en ligne sur mabanque.bnpparibas ou dans l'application Mes Comptes. Vous pouvez aussi joindre un conseiller en ligne au 3477 (service gratuit + prix appel), du lundi au vendredi de 8 h à 20 h et le samedi de 8 h à 18 h (hors jours fériés).
2. **Auprès du Responsable Réclamations Clients** : si la réponse ne vous satisfait pas, écrivez-lui via le formulaire en ligne. Ses coordonnées sont disponibles en agence, sur mabanque.bnpparibas et dans l'application Mes Comptes.
3. **Auprès d'un Médiateur**, en dernier recours amiable, gratuitement et par écrit : si vous êtes en désaccord avec la réponse de la banque, ou si vous n'avez pas reçu de réponse dans un délai de 2 mois (15 jours ouvrables pour un service de paiement, 35 jours ouvrables dans des situations exceptionnelles). Pour les opérations de banque (compte, crédit, paiements), il s'agit du Médiateur auprès de la Fédération Bancaire Française : https://lemediateur.fbf.fr. D'autres médiateurs sont compétents pour les placements financiers (AMF) et pour l'assurance.

**Délais** : si votre réclamation nécessite des recherches, la banque accuse réception sous 10 jours ouvrables et vous répond dans un délai de 2 mois maximum. Pour un service de paiement, la réponse arrive sous 15 jours ouvrables, et au plus tard sous 35 jours dans des situations exceptionnelles.

*Source : Conditions et tarifs - Particuliers, tarifs au 1er janvier 2026, « Résoudre un litige », pages 32 et 33.*""",
    "en": """I'm sorry you ran into this problem. Here is how to file a complaint.

1. **With your branch**: contact your adviser or your branch manager, in a meeting, by phone on their direct line, by mail, or through the online form on mabanque.bnpparibas or in the Mes Comptes app. You can also reach an online adviser at 3477 (free service, standard call cost), Monday to Friday from 8 am to 8 pm and Saturday from 8 am to 6 pm (except public holidays).
2. **With the Customer Complaints Manager**: if the answer doesn't satisfy you, write to them through the online form. Their contact details are available in your branch, on mabanque.bnpparibas and in the Mes Comptes app.
3. **With a Mediator**, as a last amicable resort, free of charge and in writing: if you disagree with the bank's answer, or if you haven't received an answer within 2 months (15 business days for a payment service, 35 business days in exceptional situations). For banking operations (account, credit, payments), this is the Mediator of the French Banking Federation: https://lemediateur.fbf.fr. Other mediators handle investment products (AMF) and insurance.

**Response times**: if your complaint requires investigation, the bank acknowledges it within 10 business days and answers within 2 months at most. For a payment service, the answer comes within 15 business days, and at the latest within 35 days in exceptional situations.

*Source: Conditions et tarifs - Particuliers (fee brochure), fees as of 1 January 2026, "Résoudre un litige", pages 32 and 33.*""",
}

FINANCIAL_DIFFICULTY = {
    "fr": """Je suis désolé que vous traversiez cette situation. Des solutions existent, et plus vous en parlez tôt, plus il y en a.

- **Parlez-en à votre conseiller BNP Paribas** : il pourra examiner votre situation avec vous.
- **Une offre limite les frais en cas d'incident** : le « Forfait de compte » est réservé aux clients en situation de fragilité financière. Il comprend les services essentiels (tenue de compte, carte Origin, virements et prélèvements SEPA, banque à distance, alertes SMS…) et plafonne certains frais : par exemple, la commission d'intervention est de 4 € par opération, plafonnée à 20 € par mois. Votre conseiller peut vous dire si vous pouvez en bénéficier.
- **Un accompagnement gratuit existe aussi en dehors de la banque** : les Points conseil budget, labellisés par l'État, aident gratuitement et en toute confidentialité à faire le point sur son budget. Si vos dettes deviennent impossibles à rembourser, vous pouvez déposer un dossier de surendettement auprès de la Banque de France.

*Sources : Conditions et tarifs - Particuliers, tarifs au 1er janvier 2026, page 17 (Forfait de compte). Points conseil budget et surendettement : dispositifs publics.*""",
    "en": """I'm sorry you're going through this. Solutions exist, and the earlier you talk about it, the more options you have.

- **Talk to your BNP Paribas adviser**: they can review your situation with you.
- **An offer limits fees in case of payment incidents**: the "Forfait de compte" is reserved for customers in a situation of financial fragility. It includes the essential services (account keeping, Origin card, SEPA transfers and direct debits, online banking, SMS alerts…) and caps some fees: for example, the intervention fee is 4 € per operation, capped at 20 € per month. Your adviser can tell you whether you are eligible.
- **Free support also exists outside the bank**: the Points conseil budget, labelled by the French State, provide free and confidential help to review your budget. If your debts become impossible to repay, you can file an over-indebtedness application (dossier de surendettement) with the Banque de France.

*Sources: Conditions et tarifs - Particuliers (fee brochure), fees as of 1 January 2026, page 17 (Forfait de compte). Points conseil budget and over-indebtedness: public schemes.*""",
}

CRISIS = {
    "fr": """Ce que vous traversez a l'air vraiment très difficile, et je suis désolé que vous vous sentiez ainsi. Vous n'avez pas à faire face à cela seul.

Si vous pensez à mettre fin à vos jours, appelez le **3114**, le numéro national de prévention du suicide : gratuit, 24 h/24 et 7 j/7. Des professionnels peuvent vous écouter dès maintenant.

En cas de danger immédiat, appelez le **15** (SAMU) ou le **112**.

Pour vos difficultés d'argent, des solutions existent aussi, et votre conseiller BNP Paribas peut vous aider à les trouver. Mais aujourd'hui, le plus important, c'est vous.""",
    "en": """It sounds like you're going through something really hard, and I'm sorry you feel this way. You don't have to face this alone.

If you are thinking about ending your life, please call **3114**, France's national suicide prevention line: free, 24/7. Trained professionals can listen to you right now.

If you are in immediate danger, call **112** (emergency services).

There are also solutions for money problems, and your BNP Paribas adviser can help you find them. But right now, what matters most is you.""",
}

ADVICE = {
    "fr": """Je ne peux pas vous recommander un produit ou une décision adaptés à votre situation personnelle : cela demande d'évaluer vos besoins, vos revenus et vos projets, ce que seul un conseiller BNP Paribas peut faire.

En revanche, je peux vous donner les informations des documents officiels, par exemple ce que coûte une carte ou ce qu'elle comprend. Posez-moi votre question sous cette forme, ou contactez votre conseiller pour un conseil personnalisé.""",
    "en": """I can't recommend a product or a decision for your personal situation: that requires assessing your needs, your income and your plans, which only a BNP Paribas adviser can do.

However, I can give you the information from the official documents, for example what a card costs or what it includes. Ask me your question that way, or contact your adviser for personal advice.""",
}

OFF_TOPIC = {
    "fr": """Je suis un assistant dédié aux tarifs, aux produits et aux démarches de BNP Paribas pour les particuliers clients en agence, en France métropolitaine. Je ne peux pas répondre à cette demande.

Si vous avez une question sur votre compte, vos cartes ou les frais bancaires, je serai ravi de vous aider.""",
    "en": """I'm an assistant dedicated to the fees, products and procedures of BNP Paribas's branch offer for individual customers in mainland France. I can't help with this request.

If you have a question about your account, your cards or bank fees, I'll be happy to help.""",
}

FIXED_MESSAGES = {
    "advice": ADVICE,
    "emergency": EMERGENCY,
    "complaint": COMPLAINT,
    "financial_difficulty": FINANCIAL_DIFFICULTY,
    "crisis": CRISIS,
    "off_topic": OFF_TOPIC,
}

# A short way back for customers who receive a fixed message by mistake.
RECOVERY = {
    "fr": "Si j'ai mal compris votre demande, reformulez-la et je chercherai la réponse dans les documents.",
    "en": "If I misunderstood your request, rephrase it and I'll look for the answer in the documents.",
}

CATEGORIES_WITH_RECOVERY = {"advice", "complaint", "financial_difficulty", "off_topic"}


def get_fixed_message(category: str, language: str) -> str:
    """Return the fixed message of a category, in French or English."""
    message = FIXED_MESSAGES[category][language]
    if category in CATEGORIES_WITH_RECOVERY:
        message += "\n\n" + RECOVERY[language]
    return message