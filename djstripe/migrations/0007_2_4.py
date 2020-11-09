# Generated by Django 3.1.2 on 2020-11-09 00:28

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import djstripe.enums
import djstripe.fields
import djstripe.models.api


class Migration(migrations.Migration):
    dependencies = [("djstripe", "0006_2_3")]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="payouts_enabled",
            field=models.BooleanField(
                help_text="Whether Stripe can send payouts to this account", null=True
            ),
        ),
        migrations.AlterField(
            model_name="djstripepaymentmethod",
            name="type",
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="fileupload",
            name="purpose",
            field=djstripe.fields.StripeEnumField(
                enum=djstripe.enums.FileUploadPurpose,
                help_text="The purpose of the uploaded file.",
                max_length=35,
            ),
        ),
        migrations.AddField(
            model_name="balancetransaction",
            name="reporting_category",
            field=djstripe.fields.StripeEnumField(
                default="",
                enum=djstripe.enums.BalanceTransactionReportingCategory,
                help_text="More information: https://stripe.com/docs/reports/reporting-categories",
                max_length=29,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="balancetransaction",
            name="source",
            field=djstripe.fields.StripeIdField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="applicationfee",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="applicationfeerefund",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="balancetransaction",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="bankaccount",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="card",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="charge",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="countryspec",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="coupon",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="dispute",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="fileupload",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="invoiceitem",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="paymentintent",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="payout",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="plan",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="refund",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="scheduledqueryrun",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="session",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="setupintent",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="source",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="subscriptionitem",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="taxrate",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="transfer",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="transferreversal",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="upcominginvoice",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AddField(
            model_name="usagerecord",
            name="djstripe_owner_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The Stripe Account this object belongs to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AlterField(
            model_name="paymentintent",
            name="on_behalf_of",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The account (if any) for which the funds of the PaymentIntent are intended.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payment_intents",
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.AlterField(
            model_name="setupintent",
            name="on_behalf_of",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                help_text="The account (if any) for which the setup is intended.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="setup_intents",
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
            ),
        ),
        migrations.CreateModel(
            name="APIKey",
            fields=[
                (
                    "djstripe_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "livemode",
                    models.BooleanField(
                        blank=True,
                        default=None,
                        help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.",
                        null=True,
                    ),
                ),
                (
                    "created",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="The datetime this object was created in stripe.",
                        null=True,
                    ),
                ),
                (
                    "metadata",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.",
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="A description of this object.", null=True
                    ),
                ),
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.CharField(
                        default=djstripe.models.api.generate_api_key_id,
                        editable=False,
                        max_length=255,
                    ),
                ),
                (
                    "type",
                    djstripe.fields.StripeEnumField(
                        enum=djstripe.enums.APIKeyType, max_length=11
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Key name"
                    ),
                ),
                (
                    "secret",
                    models.CharField(
                        max_length=128,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^(pk|sk|rk)_(test|live)_([a-zA-Z0-9]{24,99})"
                            )
                        ],
                    ),
                ),
                (
                    "djstripe_owner_account",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        help_text="The Stripe Account this object belongs to.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.account",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="start",
        ),
        migrations.AlterUniqueTogether(
            name="customer",
            unique_together={("subscriber", "livemode", "djstripe_owner_account")},
        ),
        migrations.AddField(
            model_name="subscription",
            name="cancel_at",
            field=djstripe.fields.StripeDateTimeField(
                blank=True,
                help_text="A date in the future at which the subscription will automatically get canceled.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="balance",
            field=djstripe.fields.StripeQuantumCurrencyAmountField(
                default=0,
                help_text="Current balance (in cents), if any, being stored on the customer's account. If negative, the customer has credit to apply to the next invoice. If positive, the customer has an amount owed that will be added to the next invoice. The balance does not refer to any unpaid invoices; it solely takes into account amounts that have yet to be successfully applied to any invoice. This balance is only taken into account for recurring billing purposes (i.e., subscriptions, invoices, invoice items).",
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="delinquent",
            field=models.BooleanField(
                default=False,
                help_text="Whether or not the latest charge for the customer's latest invoice has failed.",
            ),
        ),
        migrations.RemoveField(
            model_name="account",
            name="branding_icon",
        ),
        migrations.RemoveField(
            model_name="account",
            name="branding_logo",
        ),
        migrations.AlterField(
            model_name="bankaccount",
            name="account_holder_name",
            field=models.TextField(
                blank=True,
                help_text="The name of the person or business that owns the bank account.",
                max_length=5000,
            ),
        ),
        migrations.CreateModel(
            name="Price",
            fields=[
                (
                    "djstripe_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("id", djstripe.fields.StripeIdField(max_length=255, unique=True)),
                (
                    "livemode",
                    models.BooleanField(
                        blank=True,
                        default=None,
                        help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.",
                        null=True,
                    ),
                ),
                (
                    "created",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="The datetime this object was created in stripe.",
                        null=True,
                    ),
                ),
                (
                    "metadata",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.",
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="A description of this object.", null=True
                    ),
                ),
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                (
                    "active",
                    models.BooleanField(
                        help_text="Whether the price can be used for new purchases."
                    ),
                ),
                (
                    "currency",
                    djstripe.fields.StripeCurrencyCodeField(
                        help_text="Three-letter ISO currency code", max_length=3
                    ),
                ),
                (
                    "nickname",
                    models.CharField(
                        blank=True,
                        help_text="A brief description of the plan, hidden from customers.",
                        max_length=250,
                    ),
                ),
                (
                    "recurring",
                    djstripe.fields.JSONField(
                        blank=True,
                        default=None,
                        help_text="The recurring components of a price such as `interval` and `usage_type`.",
                        null=True,
                    ),
                ),
                (
                    "type",
                    djstripe.fields.StripeEnumField(
                        enum=djstripe.enums.PriceType,
                        help_text="Whether the price is for a one-time purchase or a recurring (subscription) purchase.",
                        max_length=9,
                    ),
                ),
                (
                    "unit_amount",
                    djstripe.fields.StripeQuantumCurrencyAmountField(
                        blank=True,
                        help_text="The unit amount in cents to be charged, represented as a whole integer if possible. Null if a sub-cent precision is required.",
                        null=True,
                    ),
                ),
                (
                    "unit_amount_decimal",
                    djstripe.fields.StripeDecimalCurrencyAmountField(
                        blank=True,
                        decimal_places=12,
                        help_text="The unit amount in cents to be charged, represented as a decimal string with at most 12 decimal places.",
                        max_digits=19,
                        null=True,
                    ),
                ),
                (
                    "billing_scheme",
                    djstripe.fields.StripeEnumField(
                        blank=True,
                        enum=djstripe.enums.BillingScheme,
                        help_text="Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.",
                        max_length=8,
                    ),
                ),
                (
                    "tiers",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`.",
                        null=True,
                    ),
                ),
                (
                    "tiers_mode",
                    djstripe.fields.StripeEnumField(
                        blank=True,
                        enum=djstripe.enums.PriceTiersMode,
                        help_text="Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows.",
                        max_length=9,
                        null=True,
                    ),
                ),
                (
                    "djstripe_owner_account",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        help_text="The Stripe Account this object belongs to.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.account",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "product",
                    djstripe.fields.StripeForeignKey(
                        help_text="The product this price is associated with.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prices",
                        to="djstripe.product",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "lookup_key",
                    models.CharField(
                        blank=True,
                        help_text="A lookup key used to retrieve prices dynamically from a static string.",
                        max_length=250,
                        null=True,
                    ),
                ),
                (
                    "transform_quantity",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="Apply a transformation to the reported usage or set quantity before computing the amount billed. Cannot be combined with `tiers`.",
                        null=True,
                    ),
                ),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
                "ordering": ["unit_amount"],
            },
        ),
        # Oddly, this is repeated. Django bug?
        migrations.AlterModelOptions(
            name="price",
            options={"ordering": ["unit_amount"]},
        ),
        migrations.AddField(
            model_name="subscriptionitem",
            name="price",
            field=models.ForeignKey(
                blank=True,
                help_text="The price the customer is subscribed to.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscription_items",
                to="djstripe.price",
            ),
        ),
        migrations.CreateModel(
            name="TaxId",
            fields=[
                (
                    "djstripe_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("id", djstripe.fields.StripeIdField(max_length=255, unique=True)),
                (
                    "livemode",
                    models.BooleanField(
                        blank=True,
                        default=None,
                        help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.",
                        null=True,
                    ),
                ),
                (
                    "created",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="The datetime this object was created in stripe.",
                        null=True,
                    ),
                ),
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                (
                    "country",
                    models.CharField(
                        help_text="Two-letter ISO code representing the country of the tax ID.",
                        max_length=2,
                    ),
                ),
                (
                    "type",
                    djstripe.fields.StripeEnumField(
                        enum=djstripe.enums.TaxIdType,
                        help_text="The status of this subscription.",
                        max_length=7,
                    ),
                ),
                (
                    "value",
                    models.CharField(help_text="Value of the tax ID.", max_length=50),
                ),
                (
                    "verification",
                    djstripe.fields.JSONField(
                        help_text="Tax ID verification information."
                    ),
                ),
                (
                    "customer",
                    djstripe.fields.StripeForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tax_ids",
                        to="djstripe.customer",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "djstripe_owner_account",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        help_text="The Stripe Account this object belongs to.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.account",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
            ],
            options={
                "verbose_name": "Tax ID",
                "verbose_name_plural": "Tax IDs",
            },
        ),
        migrations.RemoveField(
            model_name="customer",
            name="business_vat_id",
        ),
        migrations.AddField(
            model_name="invoiceitem",
            name="unit_amount",
            field=djstripe.fields.StripeQuantumCurrencyAmountField(
                blank=True,
                help_text="Unit amount (in the `currency` specified) of the invoice item.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="invoiceitem",
            name="unit_amount_decimal",
            field=djstripe.fields.StripeDecimalCurrencyAmountField(
                blank=True,
                decimal_places=12,
                help_text="Same as `unit_amount`, but contains a decimal value with at most 12 decimal places.",
                max_digits=19,
                null=True,
            ),
        ),
    ]
