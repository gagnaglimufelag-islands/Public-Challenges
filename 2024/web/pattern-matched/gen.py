import yaml
import random
import sqlite3
from string import ascii_letters, digits
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open("meta.yml"))["flags"]
DB = HERE / "src" / "db.sqlite"


def gen_random_token(length):
    alphabet = ascii_letters + digits
    former_len = random.randint(1, length - 2)
    latter_len = length - former_len - 1
    former = "".join(random.choices(alphabet, k=former_len))
    latter = "".join(random.choices(alphabet, k=latter_len))
    return f"{former}_{latter}"


conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute(
    """
CREATE TABLE IF NOT EXISTS tokens (
    valid BOOLEAN NOT NULL,
    token TEXT NOT NULL
)
"""
)

cur.execute(
    """
CREATE TABLE IF NOT EXISTS patterns (
    name TEXT NOT NULL,
    pattern TEXT NOT NULL
)
"""
)

cur.execute(
    """
INSERT INTO tokens (valid, token) VALUES (?, ?)
""",
    (True, gen_random_token(69)),
)  # hehe funny number

patterns = [
    (
        "AWS Access Key ID Value",
        "(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}",
    ),
    (
        "AWS Access Key ID Value Base64",
        "(QTNU|QUtJQ|QUdQQ|QUlEQ|QVJPQ|QUlQQ|QU5QQ|QU5WQ|QVNJQ)[%a-zA-Z0-9+/]{20,24}={0,2}",
    ),
    (
        "AWS Account ID",
        "((\\\"|'|`)?((?i)aws)?_?((?i)account)_?((?i)id)?(\\\"|'|`)?\\\\s{0,50}(:|=>|=)\\\\s{0,50}(\\\"|'|`)?[0-9]{4}-?[0-9]{4}-?[0-9]{4}(\\\"|'|`)?)",
    ),
    (
        "AWS Secret Access Key",
        "((\\\"|'|`)?((?i)aws)?_?((?i)secret)_?((?i)access)?_?((?i)key)?_?((?i)id)?(\\\"|'|`)?\\\\s{0,50}(:|=>|=)\\\\s{0,50}(\\\"|'|`)?[A-Za-z0-9/+=]{40}(\\\"|'|`)?)",
    ),
    (
        "AWS Session Token",
        "((\\\"|'|`)?((?i)aws)?_?((?i)session)?_?((?i)token)?(\\\"|'|`)?\\\\s{0,50}(:|=>|=)\\\\s{0,50}(\\\"|'|`)?[A-Za-z0-9/+=]{16,}(\\\"|'|`)?)",
    ),
    (
        "Amazon MWS Auth Token",
        "amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    ),
    ("Artifactory", "(?i)artifactory.{0,50}(\\\"|'|`)?[a-zA-Z0-9=]{112}(\\\"|'|`)?"),
    ("CC", "(?i)codeclima.{0,50}(\\\"|'|`)?[0-9a-f]{64}(\\\"|'|`)?"),
    ("Facebook Access Token", "EAACEdEose0cBA[0-9A-Za-z]+"),
    ("Facebook Access Token Base64", "RUFBQ0VkRW9zZTBjQk[%a-zA-Z0-9+/]+={0,2}"),
    ("Facebook Oauth", "(?i)facebook[^/]{0,50}(\\\"|'|`)?[0-9a-f]{32}(\\\"|'|`)?"),
    (
        "Google (GCP) Service-account",
        "((\\\"|'|`)?type(\\\"|'|`)?\\\\s{0,50}(:|=>|=)\\\\s{0,50}(\\\"|'|`)?service_account(\\\"|'|`)?,?)",
    ),
    ("Google API Key", "AIza[0-9A-Za-z\\-_]{35}"),
    ("Google API Key Base64", "QUl6Y[%a-zA-Z0-9+/]{47}"),
    ("Google OAuth", "[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com"),
    ("Google OAuth Access Token", "ya29\\.[0-9A-Za-z\\-_]+"),
    (
        "Google Oauth",
        "((\\\"|'|`)?client_secret(\\\"|'|`)?\\\\s{0,50}(:|=>|=)\\\\s{0,50}(\\\"|'|`)?[a-zA-Z0-9-_]{24}(\\\"|'|`)?)",
    ),
    (
        "Heroku API Key",
        "(?i)heroku.{0,50}[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}",
    ),
    ("Hockeyapp", "(?i)hockey.{0,50}(\\\"|'|`)?[0-9a-f]{32}(\\\"|'|`)?"),
    ("MailChimp API Key", "[0-9a-f]{32}-us[0-9]{1,2}"),
    ("Mailgun API Key", "key-[0-9a-zA-Z]{32}"),
    ("Flag", FLAG),
    ("Outlook team", "https\\://outlook\\.office.com/webhook/[0-9a-f-]{36}\\@"),
    (
        "PayPal Braintree Access Token",
        "access_token\\$production\\$[0-9a-z]{16}\\$[0-9a-f]{32}",
    ),
    ("PGP private key block", "-----BEGIN PGP PRIVATE KEY BLOCK-----"),
    (
        "PGP private key block Base64",
        "LS0tLS1CRUdJTiBQR1AgUFJJVkFURSBLRVkgQkxPQ0stLS0tL[%a-zA-Z0-9+/]+={0,2}",
    ),
    ("RSA private key", "-----BEGIN RSA PRIVATE KEY-----"),
    (
        "RSA private key Base64",
        "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tL[%a-zA-Z0-9+/]+={0,2}",
    ),
    ("SSH (DSA) private key", "-----BEGIN DSA PRIVATE KEY-----"),
    (
        "SSH (DSA) private key Base64",
        "LS0tLS1CRUdJTiBEU0EgUFJJVkFURSBLRVktLS0tL[%a-zA-Z0-9+/]+={0,2}",
    ),
    ("SSH (EC) private key", "-----BEGIN EC PRIVATE KEY-----"),
    (
        "SSH (EC) private key Base64",
        "LS0tLS1CRUdJTiBFQyBQUklWQVRFIEtFWS0tLS0t[%a-zA-Z0-9+/]+={0,2}",
    ),
    ("SSH (OPENSSH) private key", "-----BEGIN OPENSSH PRIVATE KEY-----"),
    (
        "SSH (OPENSSH) private key Base64",
        "LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS[%a-zA-Z0-9+/]+={0,2}",
    ),
    ("Sauce", "(?i)sauce.{0,50}(\\\"|'|`)?[0-9a-f-]{36}(\\\"|'|`)?"),
    ("Slack Token", "(xox[pboa]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})"),
    (
        "Slack Webhook",
        "https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}",
    ),
    ("Sonar", "(?i)sonar.{0,50}(\\\"|'|`)?[0-9a-f]{40}(\\\"|'|`)?"),
    ("Square Access Token", "sq0atp-[0-9A-Za-z\\-_]{22}"),
    ("Square OAuth Secret", "sq0csp-[0-9A-Za-z\\-_]{43}"),
    ("Stripe API Key", "sk_live_[0-9a-zA-Z]{24}"),
    ("Stripe Restricted API Key", "rk_live_[0-9a-zA-Z]{24}"),
    ("Surge", "(?i)surge.{0,50}(\\\"|'|`)?[0-9a-f]{32}(\\\"|'|`)?"),
    ("Twilio API Key", "SK[0-9a-fA-F]{32}"),
    ("Twitter Oauth", "(?i)twitter[^/]{0,50}[0-9a-zA-Z]{35,44}"),
    (
        "Password in URL",
        "[a-zA-Z]{3,10}://[^/\\s:@]{3,20}:[^/\\s:@]{3,20}@.{1,100}[\"'\\s]",
    ),
    (
        "S3 Buckets",
        "[a-z0-9.-]+\\.s3\\.amazonaws\\.com|[a-z0-9.-]+\\.s3-[a-z0-9-]\\.amazonaws\\.com|[a-z0-9.-]+\\.s3-website[.-](eu|ap|us|ca|sa|cn)|//s3\\.amazonaws\\.com/[a-z0-9._-]+|//s3-[a-z0-9-]+\\.amazonaws\\.com/[a-z0-9._-]+",
    ),
    ("Generic Private Key", "-----BEGIN [ A-Za-z0-9]*PRIVATE KEY[ A-Za-z0-9]*-----"),
    ("Generic certificate header", "-----BEGIN .{3,100}-----"),
    ("Generic certificate header Base64", "LS0tLS1CRUdJT[%a-zA-Z0-9+/]+={0,2}"),
    (
        "Generic Password",
        "(?i)pass(word)?[\\w-]*\\\\s*[=:>|]+\\s*['\"`][^'\"`]{3,100}['\"`]",
    ),
    ("Generic Secret", "(?i)secret[\\w-]*\\s*[=:>|]+\\s*['\"`][^'\"`]{3,100}['\"`]"),
    ("Generic Token", "(?i)token[\\w-]*\\s*[=:>|]+\\s*['\"`][^'\"`]{3,100}['\"`]"),
    (
        "Common secret names",
        "(?i)aws_access|aws_secret|api[_-]?key|listbucketresult|s3_access_key|authorization:|ssh-rsa AA|pass(word)?|secret|token",
    ),
    (
        "PHP Things Base64",
        "(eyJ|YTo|Tzo|PD[89]|aHR0cHM6L|aHR0cDo|rO0)[%a-zA-Z0-9+/]+={0,2}",
    ),
    (
        "IP Address",
        "\\b(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\b",
    ),
    (
        "URL",
        "[a-zA-Z]{2,10}://[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9]{1,6}\\b([-a-zA-Z0-9()@:%_\\+.~#?&//=]*)",
    ),
    ("HTTP URL Base64", "(aHR0cD|aHR0cHM6)[%a-zA-Z0-9+/]+={0,2}"),
    ("Email", "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+"),
    (
        "Hostname",
        "\\b(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9])\\.)+(com|org|net)\\b",
    ),
    ("Suspicious Comments", "(?i)\\b(hack|hax|fix|oo+ps|fuck|ugly|todo|shit)\\b"),
]

for pattern in patterns:
    cur.execute("INSERT INTO patterns (name, pattern) VALUES (?, ?)", (pattern[0], pattern[1]))

conn.commit()
cur.close()
conn.close()
